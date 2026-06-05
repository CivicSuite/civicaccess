# CivicAccess

CivicAccess is the CivicSuite module for accessibility, plain-language, multilingual, and ADA Title II review-support workflows.

Current state: **v0.2.0 corrective demotion state**. This repo contains a deterministic scaffold with a FastAPI package aligned to the published CivicCore v1.2.0 release wheel, health/root endpoints, readiness gates, WCAG-aligned review support, optional database-backed review records via `CIVICACCESS_REVIEW_DB_URL`, accessible form planning, accessible publishing workflow checks, plain-language rewrites, multilingual draft variants, ADA Title II review-support packages, tagged-PDF expectations, records-ready export checklists, and an API-backed public review UI at `/civicaccess`. The previous `v1.0.0` release was published in error and is superseded by this honest sub-1.0.0 label.

CivicAccess does **not** provide legal advice, certified ADA compliance, official translation certification, live LLM calls, or final publication approval. City staff, ADA coordinators, translators, and qualified reviewers remain responsible for publication decisions.

## What CivicAccess Does

- Reviews public content for actionable WCAG-aligned issues.
- Reports whether local review-record persistence is ready through `/ready`.
- Checks accessible form publication basics: labels, required fields, validation copy, and record context.
- Builds a staff publication workflow with accessibility, plain-language, translation-review, export, and approval steps.
- Rewrites common municipal jargon into plainer language while preserving source/rewrite provenance.
- Produces multilingual draft variants that are explicitly marked for human review.
- Produces ADA Title II review-support checklists without claiming certification.
- Checks tagged-PDF heading expectations before publication.
- Builds records-ready export checklists that preserve source/rewrite provenance.
- Provides a local API-backed accessibility review UI at `/civicaccess`.

## Release Integrity Correction

CivicAccess is not finished, shipping, city-ready, product-ready, or public-use ready. It has no real AI layer, no real municipal data/search layer, no production-grade frontend, and no independent Section 2 public-use gate sign-off. See [docs/release-integrity-correction-2026-05-21.md](docs/release-integrity-correction-2026-05-21.md).

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
- `POST /api/v1/civicaccess/review` returns accessibility findings and next steps.
- `GET /api/v1/civicaccess/reviews/{review_id}` retrieves persisted review records when `CIVICACCESS_REVIEW_DB_URL` is configured.
- `POST /api/v1/civicaccess/forms` returns accessible form publication checks.
- `POST /api/v1/civicaccess/publishing-workflow` returns staff publication workflow blockers and steps.
- `POST /api/v1/civicaccess/plain-language` returns a deterministic plain-language rewrite.
- `POST /api/v1/civicaccess/language-variant` returns a multilingual draft variant requiring human review.
- `POST /api/v1/civicaccess/ada-title-ii` returns ADA Title II review-support checklist items.
- `POST /api/v1/civicaccess/tagged-pdf` returns tagged-PDF heading expectations.
- `POST /api/v1/civicaccess/export` returns a records-ready accessibility export checklist.

Set `CIVICACCESS_REVIEW_DB_URL` to enable persistent accessibility review records. When unset, CivicAccess continues to use deterministic in-memory review behavior for local examples. `/ready` remains `not-ready` until review-record persistence is configured and schema-ready.

Use the `civicaccess-db-status` console script with the same SQLAlchemy URL to initialize and verify the local CivicAccess schema before pointing the runtime at a review database.

## License

Code is Apache 2.0. Documentation is CC BY 4.0.
