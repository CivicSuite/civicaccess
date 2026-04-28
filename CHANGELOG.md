# Changelog

All notable changes to CivicAccess will be documented in this file.

The format follows Keep a Changelog, and this project follows Semantic Versioning.

## [Unreleased]

### Added

- Production-depth accessibility review persistence slice with `CIVICACCESS_REVIEW_DB_URL`, persisted review requests/findings, and retrieval by `review_id`.

## [0.1.1] - 2026-04-28

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
