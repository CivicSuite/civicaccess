"""Records-ready accessibility export helpers for CivicAccess v0.1.0."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class AccessibleExport:
    title: str
    format: str
    checklist: tuple[str, ...]
    retention_note: str


def build_accessible_export(*, title: str, format: str = "html") -> AccessibleExport:
    """Build a deterministic records-ready export checklist."""

    return AccessibleExport(
        title=title.strip() or "Untitled accessible publication",
        format=format,
        checklist=(
            "Declare document language.",
            "Use heading order without skipped levels.",
            "Provide alt text or decorative-image marking.",
            "Preserve source text and rewrite provenance for records requests.",
        ),
        retention_note="Keep the source, rewritten text, reviewer, and publication timestamp with the municipal record.",
    )
