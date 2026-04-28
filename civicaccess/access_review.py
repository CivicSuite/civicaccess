"""Deterministic accessibility review helpers for CivicAccess v0.1.1."""

from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass
from datetime import UTC, datetime
from uuid import uuid4

import sqlalchemy as sa
from sqlalchemy import Engine, create_engine


@dataclass(frozen=True)
class AccessibilityFinding:
    code: str
    severity: str
    message: str
    fix: str
    wcag_reference: str


@dataclass(frozen=True)
class AccessibilityReview:
    status: str
    findings: tuple[AccessibilityFinding, ...]
    disclaimer: str


@dataclass(frozen=True)
class StoredAccessibilityReview:
    review_id: str
    title: str
    body: str
    has_alt_text: bool
    language: str
    status: str
    findings: tuple[AccessibilityFinding, ...]
    disclaimer: str
    created_at: datetime


DISCLAIMER = (
    "Accessibility review is advisory support only; it does not replace legal review, "
    "a certified accessibility audit, or an ADA coordinator's decision."
)


metadata = sa.MetaData()

accessibility_review_records = sa.Table(
    "accessibility_review_records",
    metadata,
    sa.Column("review_id", sa.String(36), primary_key=True),
    sa.Column("title", sa.String(500), nullable=False),
    sa.Column("body", sa.Text(), nullable=False),
    sa.Column("has_alt_text", sa.Boolean(), nullable=False),
    sa.Column("language", sa.String(80), nullable=False),
    sa.Column("status", sa.String(80), nullable=False),
    sa.Column("findings", sa.JSON(), nullable=False),
    sa.Column("disclaimer", sa.Text(), nullable=False),
    sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
    schema="civicaccess",
)


class AccessibilityReviewRepository:
    """SQLAlchemy-backed accessibility review records for local publication workflows."""

    def __init__(self, *, db_url: str | None = None, engine: Engine | None = None) -> None:
        base_engine = engine or create_engine(db_url or "sqlite+pysqlite:///:memory:", future=True)
        if base_engine.dialect.name == "sqlite":
            self.engine = base_engine.execution_options(schema_translate_map={"civicaccess": None})
        else:
            self.engine = base_engine
            with self.engine.begin() as connection:
                connection.execute(sa.text("CREATE SCHEMA IF NOT EXISTS civicaccess"))
        metadata.create_all(self.engine)

    def create_review(
        self, *, title: str, body: str, has_alt_text: bool, language: str
    ) -> StoredAccessibilityReview:
        review = review_accessibility(
            title=title,
            body=body,
            has_alt_text=has_alt_text,
            language=language,
        )
        stored = StoredAccessibilityReview(
            review_id=str(uuid4()),
            title=title,
            body=body,
            has_alt_text=has_alt_text,
            language=language,
            status=review.status,
            findings=review.findings,
            disclaimer=review.disclaimer,
            created_at=datetime.now(UTC),
        )
        with self.engine.begin() as connection:
            connection.execute(
                accessibility_review_records.insert().values(
                    review_id=stored.review_id,
                    title=stored.title,
                    body=stored.body,
                    has_alt_text=stored.has_alt_text,
                    language=stored.language,
                    status=stored.status,
                    findings=[_finding_to_dict(finding) for finding in stored.findings],
                    disclaimer=stored.disclaimer,
                    created_at=stored.created_at,
                )
            )
        return stored

    def get_review(self, review_id: str) -> StoredAccessibilityReview | None:
        with self.engine.begin() as connection:
            row = connection.execute(
                sa.select(accessibility_review_records).where(
                    accessibility_review_records.c.review_id == review_id
                )
            ).mappings().first()
        if row is None:
            return None
        return _row_to_stored_review(row)


def review_accessibility(*, title: str, body: str, has_alt_text: bool, language: str) -> AccessibilityReview:
    """Return deterministic sample accessibility findings without live LLM calls."""

    findings: list[AccessibilityFinding] = []
    if not title.strip():
        findings.append(
            AccessibilityFinding(
                code="missing-title",
                severity="high",
                message="The document needs a descriptive title.",
                fix="Add a short title that names the service, deadline, or public action.",
                wcag_reference="WCAG 2.4.2 Page Titled",
            )
        )
    if not has_alt_text:
        findings.append(
            AccessibilityFinding(
                code="missing-alt-text",
                severity="high",
                message="At least one image or visual element is missing alternative text.",
                fix="Add concise alt text that explains the purpose of the visual, or mark decorative images as decorative.",
                wcag_reference="WCAG 1.1.1 Non-text Content",
            )
        )
    if len(body.split()) > 80:
        findings.append(
            AccessibilityFinding(
                code="long-copy",
                severity="medium",
                message="The sample text is long enough to need headings or a plain-language summary.",
                fix="Break the content into sections and add a plain-language summary before the detailed text.",
                wcag_reference="WCAG 3.1.5 Reading Level",
            )
        )
    if language.strip().lower() not in {"en", "english"}:
        findings.append(
            AccessibilityFinding(
                code="language-confirmation",
                severity="medium",
                message="The document language should be declared and checked by a qualified reviewer.",
                fix="Set the document language metadata and confirm the translation with a human reviewer.",
                wcag_reference="WCAG 3.1.1 Language of Page",
            )
        )

    return AccessibilityReview(
        status="needs-fixes" if findings else "passes-sample-checks",
        findings=tuple(findings),
        disclaimer=DISCLAIMER,
    )


def _finding_to_dict(finding: AccessibilityFinding) -> dict[str, str]:
    return {
        "code": finding.code,
        "severity": finding.severity,
        "message": finding.message,
        "fix": finding.fix,
        "wcag_reference": finding.wcag_reference,
    }


def _findings_from_records(records: Iterable[dict[str, str]]) -> tuple[AccessibilityFinding, ...]:
    return tuple(AccessibilityFinding(**record) for record in records)


def _row_to_stored_review(row: object) -> StoredAccessibilityReview:
    data = dict(row)
    return StoredAccessibilityReview(
        review_id=data["review_id"],
        title=data["title"],
        body=data["body"],
        has_alt_text=data["has_alt_text"],
        language=data["language"],
        status=data["status"],
        findings=_findings_from_records(data["findings"]),
        disclaimer=data["disclaimer"],
        created_at=data["created_at"],
    )
