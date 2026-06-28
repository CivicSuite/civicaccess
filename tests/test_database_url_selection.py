"""Coverage for the Phase A persistence default: DATABASE_URL -> sync Postgres, SQLite fallback."""

from __future__ import annotations

import pytest
from sqlalchemy.engine import make_url

import civicaccess.main as main_module


@pytest.mark.parametrize(
    "raw",
    [
        "postgresql+asyncpg://civicsuite:abc123@127.0.0.1:15432/civicsuite",
        "postgres+asyncpg://u:p@h:15432/db",
        "postgresql://u:p@h:5432/db",
        "postgres://u:p@h/db",
    ],
)
def test_sync_database_url_flips_scheme_to_psycopg2(raw) -> None:
    src = make_url(raw)
    out = make_url(main_module._sync_database_url(raw))
    assert out.drivername == "postgresql+psycopg2"
    # Everything except the driver must be preserved exactly.
    assert (out.username, out.password, out.host, out.port, out.database) == (
        src.username,
        src.password,
        src.host,
        src.port,
        src.database,
    )


def test_sync_database_url_passes_through_sqlite() -> None:
    assert main_module._sync_database_url("sqlite:///x/y.db") == "sqlite:///x/y.db"


def test_sync_database_url_preserves_credentials_with_marker_substrings() -> None:
    # A password/dbname containing scheme-marker text must survive (no global str.replace mangling).
    raw = make_url("postgresql+asyncpg://u:pw@h:15432/db").set(
        password="x-postgres+asyncpg-y"
    )
    out = make_url(main_module._sync_database_url(raw.render_as_string(hide_password=False)))
    assert out.drivername == "postgresql+psycopg2"
    assert out.password == "x-postgres+asyncpg-y"
    assert out.database == "db"


def test_review_database_url_prefers_supervisor_postgres(monkeypatch) -> None:
    monkeypatch.delenv("CIVICACCESS_REVIEW_DB_URL", raising=False)
    monkeypatch.setenv(
        "DATABASE_URL", "postgresql+asyncpg://civicsuite:pw@127.0.0.1:15432/civicsuite"
    )
    assert (
        main_module._review_database_url()
        == "postgresql+psycopg2://civicsuite:pw@127.0.0.1:15432/civicsuite"
    )


def test_review_database_url_override_wins_over_supervisor(monkeypatch) -> None:
    monkeypatch.setenv(
        "DATABASE_URL", "postgresql+asyncpg://civicsuite:pw@127.0.0.1:15432/civicsuite"
    )
    monkeypatch.setenv(
        "CIVICACCESS_REVIEW_DB_URL", "postgresql+psycopg2://o:o@h:5432/override"
    )
    assert main_module._review_database_url() == "postgresql+psycopg2://o:o@h:5432/override"


def test_review_database_url_falls_back_to_sqlite(monkeypatch, tmp_path) -> None:
    monkeypatch.delenv("CIVICACCESS_REVIEW_DB_URL", raising=False)
    monkeypatch.delenv("DATABASE_URL", raising=False)
    monkeypatch.setenv("CIVICACCESS_DATA_DIR", str(tmp_path / "data"))
    url = main_module._review_database_url()
    assert url.startswith("sqlite:///")
    assert "civicaccess-reviews.db" in url
