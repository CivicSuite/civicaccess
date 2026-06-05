# Audit Lite - CivicAccess API Validation

**Date:** 2026-06-05
**Scope:** Reviewed bounded request models, actionable FastAPI validation errors, domain-preserved empty review behavior, and regression tests.
**Reviewer:** Codex (audit-lite)

## TL;DR

Ship this slice. CivicAccess now bounds public API payloads and returns actionable validation errors without breaking the domain-level empty-content review finding.

## Severity rollup

- Blocker: 0
- Critical: 0
- Major: 0
- Minor: 0
- Nit: 0

## Findings

None.

## What's working

- `civicaccess/main.py` adds `Field` limits for public request models and avoids mutable list defaults with `default_factory`.
- The `RequestValidationError` handler returns `message`, `fix`, and `fields` instead of FastAPI's default raw validation list.
- The review `body` remains required and bounded, while empty strings still reach the accessibility domain logic and return `missing-body`.
- Regression tests cover missing required body, oversized body, successful review, and empty-content advisory findings.

## Verification

- Focused validation/API tests - 3 passed.
- `python -m pytest -q` - 23 passed.
- `python -m ruff check .` - passed.
- `bash scripts/verify-release.sh` - PASSED; 23 passed, 1 pytest-asyncio deprecation warning, ruff passed, artifacts built.

## Escalation recommendation

No escalation needed for this slice.
