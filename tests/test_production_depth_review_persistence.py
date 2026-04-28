from fastapi.testclient import TestClient

import civicaccess.main as main_module
from civicaccess.access_review import AccessibilityReviewRepository
from civicaccess.main import app


client = TestClient(app)


def test_accessibility_review_records_persist_findings(tmp_path) -> None:
    db_path = tmp_path / "reviews.db"
    repository = AccessibilityReviewRepository(db_url=f"sqlite:///{db_path}")

    stored = repository.create_review(
        title="",
        body="Short public notice.",
        has_alt_text=False,
        language="en",
    )
    repository.engine.dispose()

    second_repository = AccessibilityReviewRepository(db_url=f"sqlite:///{db_path}")
    try:
        reloaded = second_repository.get_review(stored.review_id)
    finally:
        second_repository.engine.dispose()

    assert reloaded is not None
    assert reloaded.status == "needs-fixes"
    assert [finding.code for finding in reloaded.findings] == ["missing-title", "missing-alt-text"]
    db_path.unlink()


def test_api_persists_and_retrieves_review_records(monkeypatch, tmp_path) -> None:
    db_path = tmp_path / "api-reviews.db"
    monkeypatch.setenv("CIVICACCESS_REVIEW_DB_URL", f"sqlite:///{db_path}")

    try:
        create_response = client.post(
            "/api/v1/civicaccess/review",
            json={"title": "", "body": "A public notice.", "has_alt_text": False, "language": "en"},
        )
        review_id = create_response.json()["review_id"]
        get_response = client.get(f"/api/v1/civicaccess/reviews/{review_id}")
    finally:
        main_module._dispose_review_repository()
        main_module._review_db_url = None

    assert create_response.status_code == 200
    assert review_id
    assert create_response.json()["status"] == "needs-fixes"
    assert get_response.status_code == 200
    assert get_response.json()["review_id"] == review_id
    assert get_response.json()["findings"][0]["code"] == "missing-title"
    db_path.unlink()


def test_review_record_lookup_requires_configured_database() -> None:
    response = client.get("/api/v1/civicaccess/reviews/not-configured")

    assert response.status_code == 503
    assert "Set CIVICACCESS_REVIEW_DB_URL" in response.json()["detail"]["fix"]
