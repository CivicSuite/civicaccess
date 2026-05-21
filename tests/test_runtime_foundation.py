from fastapi.testclient import TestClient

import civicaccess
from civicaccess.main import app


client = TestClient(app)


def test_package_version_is_100() -> None:
    assert civicaccess.__version__ == "1.0.0"


def test_root_endpoint_states_runtime_boundary() -> None:
    response = client.get("/")
    assert response.status_code == 200
    payload = response.json()

    assert payload["name"] == "CivicAccess"
    assert payload["version"] == "1.0.0"
    assert payload["status"] == "public-use accessibility support release"
    assert "database-backed review records" in payload["message"]
    assert "does not provide legal advice" in payload["message"]
    assert payload["next_step"].startswith("Operate CivicAccess")


def test_health_endpoint_reports_versions() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    payload = response.json()

    assert payload["status"] == "ok"
    assert payload["service"] == "civicaccess"
    assert payload["version"] == "1.0.0"
    assert payload["civiccore_version"] == "1.1.0"
