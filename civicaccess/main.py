"""FastAPI runtime foundation for CivicAccess."""

import os

from civiccore import __version__ as CIVICCORE_VERSION
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from civicaccess import __version__
from civicaccess.access_review import AccessibilityReviewRepository, StoredAccessibilityReview, review_accessibility
from civicaccess.exports import build_accessible_export
from civicaccess.multilingual import create_language_variant
from civicaccess.plain_language import rewrite_plain_language
from civicaccess.public_ui import render_public_lookup_page


app = FastAPI(
    title="CivicAccess",
    version=__version__,
    description="Accessibility, plain-language, multilingual, and ADA review support for CivicSuite.",
)

_review_repository: AccessibilityReviewRepository | None = None
_review_db_url: str | None = None


class AccessibilityReviewRequest(BaseModel):
    title: str = ""
    body: str
    has_alt_text: bool = False
    language: str = "en"


class PlainLanguageRequest(BaseModel):
    text: str


class LanguageVariantRequest(BaseModel):
    text: str
    language: str


class AccessibleExportRequest(BaseModel):
    title: str
    format: str = "html"


@app.get("/")
def root() -> dict[str, str]:
    """Return current product state without overstating unshipped behavior."""

    return {
        "name": "CivicAccess",
        "version": __version__,
        "status": "accessibility foundation plus review persistence",
        "message": (
            "CivicAccess package, API foundation, sample accessibility review, optional database-backed review records, plain-language rewrite, multilingual variant, records-ready export checklist, and public UI foundation are online; "
            "certified ADA review, live LLM calls, production translation workflows, and document-ingestion integrations are not implemented yet."
        ),
        "next_step": "Post-v0.1.1 roadmap: certified review workflows, document ingestion, and suite-wide accessibility APIs",
    }


@app.get("/health")
def health() -> dict[str, str]:
    """Return dependency/version health for deployment smoke checks."""

    return {
        "status": "ok",
        "service": "civicaccess",
        "version": __version__,
        "civiccore_version": CIVICCORE_VERSION,
    }


@app.get("/civicaccess", response_class=HTMLResponse)
def public_civicaccess_page() -> str:
    """Return the accessible public sample UI."""

    return render_public_lookup_page()


@app.post("/api/v1/civicaccess/review")
def accessibility_review(request: AccessibilityReviewRequest) -> dict[str, object]:
    if _review_database_url() is not None:
        stored = _get_review_repository().create_review(
            title=request.title,
            body=request.body,
            has_alt_text=request.has_alt_text,
            language=request.language,
        )
        return _stored_review_response(stored)

    result = review_accessibility(
        title=request.title,
        body=request.body,
        has_alt_text=request.has_alt_text,
        language=request.language,
    )
    return {
        "status": result.status,
        "findings": [finding.__dict__ for finding in result.findings],
        "disclaimer": result.disclaimer,
        "review_id": None,
    }


@app.get("/api/v1/civicaccess/reviews/{review_id}")
def get_accessibility_review(review_id: str) -> dict[str, object]:
    if _review_database_url() is None:
        raise HTTPException(
            status_code=503,
            detail={
                "message": "CivicAccess review persistence is not configured.",
                "fix": "Set CIVICACCESS_REVIEW_DB_URL to retrieve persisted accessibility review records.",
            },
        )
    stored = _get_review_repository().get_review(review_id)
    if stored is None:
        raise HTTPException(
            status_code=404,
            detail={
                "message": "Accessibility review record not found.",
                "fix": "Use a review_id returned by POST /api/v1/civicaccess/review.",
            },
        )
    return _stored_review_response(stored)


@app.post("/api/v1/civicaccess/plain-language")
def plain_language_rewrite(request: PlainLanguageRequest) -> dict[str, object]:
    result = rewrite_plain_language(request.text)
    return result.__dict__


@app.post("/api/v1/civicaccess/language-variant")
def language_variant(request: LanguageVariantRequest) -> dict[str, object]:
    result = create_language_variant(text=request.text, language=request.language)
    return result.__dict__


@app.post("/api/v1/civicaccess/export")
def accessible_export(request: AccessibleExportRequest) -> dict[str, object]:
    result = build_accessible_export(title=request.title, format=request.format)
    return {"title": result.title, "format": result.format, "checklist": list(result.checklist), "retention_note": result.retention_note}


def _review_database_url() -> str | None:
    return os.environ.get("CIVICACCESS_REVIEW_DB_URL")


def _get_review_repository() -> AccessibilityReviewRepository:
    global _review_db_url, _review_repository
    db_url = _review_database_url()
    if db_url is None:
        raise RuntimeError("CIVICACCESS_REVIEW_DB_URL is not configured.")
    if _review_repository is None or db_url != _review_db_url:
        _dispose_review_repository()
        _review_db_url = db_url
        _review_repository = AccessibilityReviewRepository(db_url=db_url)
    return _review_repository


def _dispose_review_repository() -> None:
    global _review_repository
    if _review_repository is not None:
        _review_repository.engine.dispose()
        _review_repository = None


def _stored_review_response(stored: StoredAccessibilityReview) -> dict[str, object]:
    return {
        "review_id": stored.review_id,
        "status": stored.status,
        "findings": [finding.__dict__ for finding in stored.findings],
        "disclaimer": stored.disclaimer,
        "title": stored.title,
        "language": stored.language,
        "created_at": stored.created_at.isoformat(),
    }
