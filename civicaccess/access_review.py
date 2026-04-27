"""Deterministic accessibility review helpers for CivicAccess v0.1.0."""

from __future__ import annotations

from dataclasses import dataclass


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


DISCLAIMER = (
    "Accessibility review is advisory support only; it does not replace legal review, "
    "a certified accessibility audit, or an ADA coordinator's decision."
)


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
