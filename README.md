# CivicAccess

CivicAccess is the CivicSuite module for accessibility, plain-language, multilingual, and ADA Title II review-support workflows.

Current state: **v1.0.0 public-use support release**. This repo ships a FastAPI package, health/root endpoints, deterministic WCAG-aligned review support, optional database-backed review records via `CIVICACCESS_REVIEW_DB_URL`, accessible form planning, accessible publishing workflow checks, plain-language rewrites, multilingual draft variants, ADA Title II review-support packages, tagged-PDF expectations, records-ready export checklists, a functional public UI at `/civicaccess`, and `civiccore==1.1.0` dependency alignment.

CivicAccess does **not** provide legal advice, certified ADA compliance, official translation certification, live LLM calls, or final publication approval. City staff, ADA coordinators, translators, and qualified reviewers remain responsible for publication decisions.

## What CivicAccess Does

- Reviews public content for actionable WCAG-aligned issues.
- Checks accessible form publication basics: labels, required fields, validation copy, and record context.
- Builds a staff publication workflow with accessibility, plain-language, translation-review, export, and approval steps.
- Rewrites common municipal jargon into plainer language while preserving source/rewrite provenance.
- Produces multilingual draft variants that are explicitly marked for human review.
- Produces ADA Title II review-support checklists without claiming certification.
- Checks tagged-PDF heading expectations before publication.
- Builds records-ready export checklists that preserve source/rewrite provenance.
- Provides a functional public accessibility support UI at `/civicaccess`.

## Developer Quickstart

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
python -m pytest -q
bash scripts/verify-release.sh
```

## Runtime API

- `GET /` returns current module status and boundaries.
- `GET /health` returns package and CivicCore version information.
- `GET /civicaccess` returns the public UI.
- `POST /api/v1/civicaccess/review` returns accessibility findings and next steps.
- `GET /api/v1/civicaccess/reviews/{review_id}` retrieves persisted review records when `CIVICACCESS_REVIEW_DB_URL` is configured.
- `POST /api/v1/civicaccess/forms` returns accessible form publication checks.
- `POST /api/v1/civicaccess/publishing-workflow` returns staff publication workflow blockers and steps.
- `POST /api/v1/civicaccess/plain-language` returns a deterministic plain-language rewrite.
- `POST /api/v1/civicaccess/language-variant` returns a multilingual draft variant requiring human review.
- `POST /api/v1/civicaccess/ada-title-ii` returns ADA Title II review-support checklist items.
- `POST /api/v1/civicaccess/tagged-pdf` returns tagged-PDF heading expectations.
- `POST /api/v1/civicaccess/export` returns a records-ready accessibility export checklist.

Set `CIVICACCESS_REVIEW_DB_URL` to enable persistent accessibility review records. When unset, CivicAccess continues to use deterministic in-memory review behavior for local examples.

## License

Code is Apache 2.0. Documentation is CC BY 4.0.
