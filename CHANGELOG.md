# Changelog

All notable changes to CivicAccess will be documented in this file.

The format follows Keep a Changelog, and this project follows Semantic Versioning.

## [Unreleased]

### Added

- Added default local SQLite review persistence so installed CivicAccess is ready without hidden environment setup.
- Added `/civicaccess/staff` for saved review queue, readiness, integration contracts, and records-ready export operations.
- Added `GET /api/v1/civicaccess/reviews`, `POST /api/v1/civicaccess/reviews/{review_id}/records-export`, and `GET /api/v1/civicaccess/integration-contracts`.

### Changed

- Aligned CivicAccess to the published CivicCore v1.2.0 release wheel and SHA256.
- Wired the public `/civicaccess` review form to the accessibility review API.
- Added local schema status and `/ready` readiness gates for review-record persistence.
- Added bounded request models and actionable validation errors for public API payloads.
- Changed readiness from environment-gated optional persistence to default local persistence with explicit override support.

## [0.2.0] - 2026-05-21

### Corrected

- Corrected the false `v1.0.0` release label after the independent CivicSuite release-integrity audit found CivicAccess does not meet the Section 2 FINISHED and SHIPPING bar.
- Set the honest current label to `v0.2.0` and superseded the mistaken `v1.0.0` posture without deleting the historical record.
- Current classification: scaffold - deterministic accessibility/plain-language support exists, but real AI, real municipal data/search, production-grade frontend, and public-use gate proof remain absent.
- CivicAccess must not be described as finished, shipping, city-ready, product-ready, or public-use ready until a future independent audit signs off against the full Section 2 gate.

## [1.0.0] - 2026-05-21

### Added

- Public-use CivicAccess support release covering accessible forms, accessible publishing workflow checks, WCAG-aligned review support, plain-language rewrites, multilingual draft variants, ADA Title II review-support packages, tagged-PDF expectations, records-ready exports, and a functional `/civicaccess` UI.
- New deterministic workflow endpoints for forms, publishing workflow, ADA Title II review support, and tagged-PDF expectations.
- Adversarial tests for empty content, unsupported language placeholders, unsupported export formats, blocked publishing workflows, missing persisted records, unavailable persistence, and non-certification boundaries.
- Browser QA evidence for desktop and mobile public UI states.

### Changed

- Aligned CivicAccess to `civiccore==1.1.0`.
- Updated release gates, CI, documentation, and package artifacts for `1.0.0`.

## [0.1.1] - 2026-04-28

### Added

- Production-depth accessibility review persistence slice with `CIVICACCESS_REVIEW_DB_URL`, persisted review requests/findings, and retrieval by `review_id`.

### Changed

- Aligned CivicAccess to `civiccore==0.3.0` while preserving the v0.1 accessibility foundation behavior.
- Updated version surfaces, release gate, CI CivicCore wheel install, documentation, and health-contract tests for the v0.1.1 dependency-alignment release.

## [0.1.0] - 2026-04-27

### Added

- Professional repository scaffold, documentation, issue templates, PR template, and release gates.
- FastAPI runtime foundation with root, health, and public UI endpoints.
- Deterministic sample accessibility review with WCAG-aligned actionable findings.
- Plain-language rewrite helper with human-review boundary.
- Multilingual variant helper with human-review boundary.
- Records-ready accessible export checklist.
- Accessible public sample UI at `/civicaccess` with browser QA coverage.
