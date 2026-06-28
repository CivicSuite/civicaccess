# CivicAccess City-Core Probe Progress

Tracks the city-core readiness probe gaps for CivicAccess. The probe demoted CivicAccess from
city-core (`excluded_from_city_core_needs_work_probe`) until these gaps are closed with evidence.

Phase A (this release, **v0.4.0**) closes the module-repo gaps #1–#4. Gaps #5–#6 are integration/QA
gaps owned by later phases of the CivicAccess → city-core plan
(`CivicSuite/civicsuite` → `docs/roadmap/civicaccess-citycore-integration/`).

| Gap | Description | Status | Evidence |
|-----|-------------|--------|----------|
| #1 | Clean install with the published CivicCore v1.2.0 wheel pin | **Closed** (v0.3.0) | `pyproject.toml` pins `civiccore` to the v1.2.0 release wheel + SHA256; `tests/test_runtime_foundation.py::test_pyproject_uses_published_civiccore_release_wheel` (and asserts the bad `civiccore==1.1.0`/`1.0.0` pins are absent). CI installs the wheel and asserts `civiccore.__version__ == "1.2.0"`. |
| #2 | Staff/public authz boundary on persistent writes | **Closed** (v0.4.0) | Trusted-write guard `_authorize_persistent_write` (`civicaccess/main.py`) on `POST /api/v1/civicaccess/review` and `POST /api/v1/civicaccess/reviews/{id}/records-export` — requires `CIVICACCESS_TRUSTED_WRITE_TOKEN` via `X-CivicAccess-Write-Token`; 403 on missing/invalid, 503 fail-closed when unconfigured. Public surface uses the new stateless `POST /api/v1/civicaccess/analyze` (no persistence, no token). Tests: `tests/test_citycore_hardening.py::test_review_write_rejects_missing_and_wrong_token`, `::test_records_export_write_requires_token`, `::test_write_guard_not_configured_returns_503`, `::test_analyze_is_open_and_never_persists`. |
| #3 | Module audit logging on writes/exports | **Closed** (v0.4.0) | `audit_events` table (`civicaccess/access_review.py`) + `record_audit_event`; `review.create` is written in the same transaction as the review, `review.records_export` on export. Tests: `tests/test_citycore_hardening.py::test_audit_event_persisted_on_review_create`, `::test_audit_event_persisted_on_records_export`; Postgres-side in `tests/test_postgres_persistence.py`. |
| #4 | Backup/restore proof (not declaration) | **Closed** (v0.4.0) | Default store (Postgres) durability: `tests/test_postgres_persistence.py::test_postgres_review_and_audit_survive_reconnect` writes a review + audit, disposes the engine (simulated process restart), reconnects with a fresh engine, and asserts both reload — the property the supervisor's wholesale `Data/postgres` backup relies on. Dev fallback (SQLite): `tests/test_citycore_hardening.py::test_backup_restore_roundtrip_preserves_records_and_audit` backs up the live Data file, loses it, restores, and asserts records + audit survive. The supervisor's end-to-end backup/restore on a clean VM is exercised in Phase D. |
| #5 | Installer / desktop registry record (6-module city-core) | **Deferred → Phases B–C** | The `civicaccess` record in `CivicSuite/civicsuite` `installer/modules.json` still carries the stale `civiccore_requirement: "1.1.0"` and lacks the full contract fields. Authoring the runtime-valid record (Phase B) and flipping the city-core profile to 6 modules (Phase C) are out of scope for the module repo. |
| #6 | Clean-VM browser QA + full accessibility acceptance | **Deferred → Phase D** | Exercised on a clean VM (Windows Sandbox) against the installer-built stack with a full accessibility + export-correctness acceptance pass. |

## Phase A persistence model (v0.4.0)

- **Default store:** the shared CivicCore PostgreSQL. The module reads the supervisor-injected
  `DATABASE_URL` (`postgresql+asyncpg://…:15432/…`) and derives a sync psycopg2 URL via
  `_sync_database_url` (`civicaccess/main.py`).
- **Override:** `CIVICACCESS_REVIEW_DB_URL` (a dev SQLite path or a pre-built Postgres URL).
- **Fallback:** SQLite under `CIVICACCESS_DATA_DIR` only when neither is set (explicit dev use).
- **Release gate:** `CIVICACCESS_POSTGRES_TEST_URL` is required by `scripts/verify-release.sh` and CI
  (a `postgres:16` service), so PostgreSQL persistence coverage cannot be silently skipped.

## Notes / deliberate decisions

- `POST /api/v1/civicaccess/export` (the generic export-checklist builder) is **not** token-guarded:
  it is stateless advisory compute with no persisted data, in the same class as the form/plain-language/
  workflow planning routes. The records-grade export that reads persisted data
  (`/reviews/{id}/records-export`) **is** guarded. This is the correct reading of "every
  persistence-write route".
- The write token is **never embedded in served HTML**. The staff surface provides a field where the
  operator pastes the token; it is kept in the browser session (`sessionStorage`) and sent as
  `X-CivicAccess-Write-Token` on save/export only. The token gates the API for all callers and fails
  closed (503) when `CIVICACCESS_TRUSTED_WRITE_TOKEN` is unconfigured. The token comparison is
  constant-time (`hmac.compare_digest`).
