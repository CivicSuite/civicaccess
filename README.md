# CivicAccess

CivicAccess is the CivicSuite module for accessibility, plain-language, multilingual, and ADA Title II review-support workflows.

Current state: **v0.3.0 standalone readiness candidate**. This repo contains a FastAPI package aligned to the published CivicCore v1.2.0 release wheel, health/root endpoints, readiness gates, WCAG-aligned review support, local database-backed review records, accessible form planning, accessible publishing workflow checks, plain-language rewrites, multilingual draft variants, ADA Title II review-support packages, tagged-PDF expectations, records-ready export checklists, an API-backed public review UI at `/civicaccess`, and a staff review/export workspace at `/civicaccess/staff`. The previous `v1.0.0` release was published in error and remains historical evidence only.

CivicAccess does **not** provide legal advice, certified ADA compliance, official translation certification, live LLM calls, or final publication approval. City staff, ADA coordinators, translators, and qualified reviewers remain responsible for publication decisions.

## What CivicAccess Does

- Reviews public content for actionable WCAG-aligned issues.
- Reports local review-record persistence readiness through `/ready`.
- Provides a staff queue for saved accessibility reviews and records-ready exports.
- Checks accessible form publication basics: labels, required fields, validation copy, and record context.
- Builds a staff publication workflow with accessibility, plain-language, translation-review, export, and approval steps.
- Rewrites common municipal jargon into plainer language while preserving source/rewrite provenance.
- Produces multilingual draft variants that are explicitly marked for human review.
- Produces ADA Title II review-support checklists without claiming certification.
- Checks tagged-PDF heading expectations before publication.
- Builds records-ready export checklists that preserve source/rewrite provenance.
- Provides a local API-backed accessibility review UI at `/civicaccess`.

## Release Integrity Correction

CivicAccess was previously demoted after a false `v1.0.0` release. The current branch is rebuilding that truthfully: it now has automatic local persistence, a staff workspace, and integration contracts, but it still must pass the current module-completion audit, suite integration proof, and clean-machine evidence before any finished/public-use label can be promoted. See [docs/release-integrity-correction-2026-05-21.md](docs/release-integrity-correction-2026-05-21.md).

## Developer Quickstart

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install https://github.com/CivicSuite/civiccore/releases/download/v1.2.0/civiccore-1.2.0-py3-none-any.whl
python -m pip install -e ".[dev]"
python -m pytest -q
bash scripts/verify-release.sh
```

## Runtime API

- `GET /` returns current module status and boundaries.
- `GET /health` returns package and CivicCore version information.
- `GET /ready` and `GET /api/v1/civicaccess/readiness` report whether local review persistence is configured and schema-ready.
- `GET /civicaccess` returns the API-backed public accessibility review UI.
- `GET /civicaccess/staff` returns the staff review queue and records-export workspace.
- `POST /api/v1/civicaccess/review` returns accessibility findings and next steps.
- `GET /api/v1/civicaccess/reviews` lists saved review records.
- `GET /api/v1/civicaccess/reviews/{review_id}` retrieves persisted review records.
- `POST /api/v1/civicaccess/reviews/{review_id}/records-export` builds a CivicRecords-ready retention export.
- `GET /api/v1/civicaccess/integration-contracts` publishes upstream/downstream integration contracts.
- `POST /api/v1/civicaccess/forms` returns accessible form publication checks.
- `POST /api/v1/civicaccess/publishing-workflow` returns staff publication workflow blockers and steps.
- `POST /api/v1/civicaccess/plain-language` returns a deterministic plain-language rewrite.
- `POST /api/v1/civicaccess/language-variant` returns a multilingual draft variant requiring human review.
- `POST /api/v1/civicaccess/ada-title-ii` returns ADA Title II review-support checklist items.
- `POST /api/v1/civicaccess/tagged-pdf` returns tagged-PDF heading expectations.
- `POST /api/v1/civicaccess/export` returns a records-ready accessibility export checklist.

By default, CivicAccess stores review records in `data/civicaccess-reviews.db` under the process working directory. Set `CIVICACCESS_DATA_DIR` to choose a different local data directory, or set `CIVICACCESS_REVIEW_DB_URL` to use an explicit SQLAlchemy database URL. `/ready` is expected to be ready when the local schema can be created and verified.

Use the `civicaccess-db-status` console script with an explicit SQLAlchemy URL when an operator wants to preflight a non-default review database.

## License

Code is Apache 2.0. Documentation is CC BY 4.0.
