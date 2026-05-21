# CivicAccess v1.0.0 False Release Evidence

Date: 2026-05-21

## Scope

This file is historical evidence for the mistaken 2026-05-21 v1.0.0 release. CivicAccess is now demoted to v0.2.0; do not use this file as proof that CivicAccess is finished, shipping, city-ready, product-ready, or public-use ready.

- Accessible forms.
- Accessible publishing workflow.
- WCAG review support.
- Plain-language rewrites.
- Multilingual variants.
- ADA Title II review support.
- Tagged-heading PDF expectations.
- Records-ready accessible exports.

## Runtime Surface

- `GET /`
- `GET /health`
- `GET /civicaccess`
- `POST /api/v1/civicaccess/review`
- `GET /api/v1/civicaccess/reviews/{review_id}`
- `POST /api/v1/civicaccess/forms`
- `POST /api/v1/civicaccess/publishing-workflow`
- `POST /api/v1/civicaccess/plain-language`
- `POST /api/v1/civicaccess/language-variant`
- `POST /api/v1/civicaccess/ada-title-ii`
- `POST /api/v1/civicaccess/tagged-pdf`
- `POST /api/v1/civicaccess/export`

## Boundaries

CivicAccess does not provide legal advice, certified ADA compliance, official translation certification, live LLM calls, or final publication approval.

## Local Evidence

Evidence must be refreshed before merge:

- `python -m pytest -q`
- `bash scripts/verify-docs.sh`
- `python -m ruff check .`
- `bash scripts/verify-release.sh`
- Browser QA summary at `docs/browser-qa-civicaccess-v1-summary.md`

## Browser Evidence

- Desktop render: `docs/browser-qa-civicaccess-v1-desktop.png`
- Desktop states: `docs/browser-qa-civicaccess-v1-desktop-states.png`
- Mobile render: `docs/browser-qa-civicaccess-v1-mobile.png`
- Result JSON: `docs/browser-qa-civicaccess-v1-results.json`
