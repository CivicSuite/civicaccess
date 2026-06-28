"""PostgreSQL persistence coverage. Gated on CIVICACCESS_POSTGRES_TEST_URL (the release gate)."""

from __future__ import annotations

import os

import pytest
import sqlalchemy as sa

from civicaccess.access_review import AccessibilityReviewRepository


@pytest.mark.skipif(
    not os.environ.get("CIVICACCESS_POSTGRES_TEST_URL"),
    reason="CIVICACCESS_POSTGRES_TEST_URL is required for PostgreSQL persistence coverage.",
)
def test_postgres_persistence_creates_schema_and_round_trips_reviews() -> None:
    db_url = os.environ["CIVICACCESS_POSTGRES_TEST_URL"]
    engine = sa.create_engine(db_url, future=True)
    with engine.begin() as connection:
        connection.execute(sa.text("DROP SCHEMA IF EXISTS civicaccess CASCADE"))
    engine.dispose()

    repository = AccessibilityReviewRepository(db_url=db_url)
    stored = repository.create_review(
        title="Budget hearing notice",
        body="Residents may ask for help before the hearing.",
        has_alt_text=True,
        language="en",
    )
    repository.record_audit_event(action="review.records_export", subject_id=stored.review_id)

    reloaded = repository.get_review(stored.review_id)
    assert reloaded is not None
    assert reloaded.review_id == stored.review_id
    assert reloaded.title == "Budget hearing notice"

    actions = {event["action"] for event in repository.list_audit_events()}
    assert actions == {"review.create", "review.records_export"}

    status = repository.schema_status()
    assert status.ready is True
    assert status.dialect == "postgresql"

    with repository.engine.begin() as connection:
        schema_exists = connection.execute(
            sa.text(
                "select exists(select 1 from information_schema.schemata "
                "where schema_name='civicaccess')"
            )
        ).scalar_one()
    repository.engine.dispose()
    assert schema_exists is True
