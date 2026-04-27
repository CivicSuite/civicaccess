from fastapi.testclient import TestClient

from civicaccess.access_review import review_accessibility
from civicaccess.exports import build_accessible_export
from civicaccess.main import app
from civicaccess.multilingual import create_language_variant
from civicaccess.plain_language import rewrite_plain_language


client = TestClient(app)


def test_accessibility_review_returns_actionable_findings() -> None:
    result = review_accessibility(title="", body="Short public notice.", has_alt_text=False, language="en")

    assert result.status == "needs-fixes"
    assert result.findings[0].code == "missing-title"
    assert result.findings[0].fix
    assert result.findings[1].wcag_reference == "WCAG 1.1.1 Non-text Content"
    assert "does not replace legal review" in result.disclaimer


def test_plain_language_rewrite_keeps_human_review_boundary() -> None:
    result = rewrite_plain_language("Residents must remit payment prior to the deadline.")

    assert "pay before" in result.rewritten
    assert result.review_required is True
    assert "certified accessibility audit" in result.disclaimer


def test_language_variant_is_sample_and_review_required() -> None:
    result = create_language_variant(text="Contact the city for help.", language="es")

    assert result.language == "es"
    assert "comunÃ­quese" in result.text
    assert result.review_required is True


def test_accessible_export_preserves_records_context() -> None:
    result = build_accessible_export(title="Budget Hearing Notice")

    assert result.title == "Budget Hearing Notice"
    assert "Preserve source text and rewrite provenance for records requests." in result.checklist
    assert "municipal record" in result.retention_note


def test_api_review_success_shape() -> None:
    response = client.post(
        "/api/v1/civicaccess/review",
        json={"title": "", "body": "A public notice.", "has_alt_text": False, "language": "en"},
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "needs-fixes"
    assert payload["findings"][0]["fix"]


def test_api_plain_language_and_language_variant() -> None:
    plain = client.post(
        "/api/v1/civicaccess/plain-language",
        json={"text": "Please remit payment prior to the deadline."},
    )
    variant = client.post(
        "/api/v1/civicaccess/language-variant",
        json={"text": "Contact the city for help.", "language": "vi"},
    )

    assert plain.status_code == 200
    assert "pay before" in plain.json()["rewritten"]
    assert variant.status_code == 200
    assert variant.json()["review_required"] is True


def test_public_ui_route_is_accessible_and_honest() -> None:
    response = client.get("/civicaccess")

    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    text = response.text
    assert '<a class="skip-link" href="#main">Skip to main content</a>' in text
    assert '<main id="main" tabindex="-1">' in text
    assert "v0.1.0 accessibility foundation" in text
    assert "does not provide legal advice" in text
    assert "certified accessibility audits" in text
    assert "zoning" not in text.casefold()
