# CivicAccess

CivicAccess is the CivicSuite module for accessibility, plain-language, multilingual, and ADA review support.

Current state: **v0.1.0 accessibility foundation release**. This repo ships a FastAPI package, health/root endpoints, documentation gates, deterministic sample accessibility review, plain-language rewrite, multilingual variant, records-ready export checklist, and accessible public sample UI at `/civicaccess`. It does **not** ship certified ADA compliance, legal advice, live LLM calls, production translation workflows, document ingestion, or suite-wide integration APIs.

## What CivicAccess Does

- Reviews sample public content for actionable WCAG-aligned issues.
- Rewrites common municipal jargon into plainer language while requiring human review.
- Produces sample multilingual variants that are explicitly marked for human review.
- Builds records-ready export checklists that preserve source/rewrite provenance.
- Demonstrates a public accessibility review UI at `/civicaccess`.

## Developer Quickstart

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
python -m pytest -q
bash scripts/verify-release.sh
```

## API Foundation

- `GET /` returns current module status and next roadmap boundary.
- `GET /health` returns package and CivicCore version information.
- `GET /civicaccess` returns the accessible public sample UI.
- `POST /api/v1/civicaccess/review` returns sample accessibility findings.
- `POST /api/v1/civicaccess/plain-language` returns a deterministic sample rewrite.
- `POST /api/v1/civicaccess/language-variant` returns a sample multilingual variant requiring human review.
- `POST /api/v1/civicaccess/export` returns a records-ready accessibility export checklist.

## License

Code is Apache 2.0. Documentation is CC BY 4.0.
