# Audit Lite - CivicAccess CivicCore 1.2 Alignment

**Date:** 2026-06-05
**Scope:** Reviewed the CivicAccess dependency, CI, docs, and runtime tests changed to align with the published CivicCore v1.2.0 release wheel.
**Reviewer:** Codex (audit-lite)

## TL;DR

Ship this slice. CivicAccess now installs CivicCore from the pinned v1.2.0 release wheel with SHA256, the runtime health contract expects 1.2.0, and current-facing docs no longer describe the stale 1.1.0 dependency posture.

## Severity rollup

- Blocker: 0
- Critical: 0
- Major: 0
- Minor: 0
- Nit: 0

## Findings

None.

## What's working

- `pyproject.toml` uses the published CivicCore v1.2.0 release wheel and enables Hatch direct references.
- `.github/workflows/verify.yml` installs the same CivicCore v1.2.0 wheel before the package.
- `tests/test_runtime_foundation.py` asserts both the direct-reference dependency and the `/health` CivicCore version.
- README, user manual, docs landing, implementation plan, and placeholder-import diagnostics all reflect the 1.2.0 platform alignment.

## Verification

- `python -m pytest tests\test_runtime_foundation.py -q` - 4 passed.
- `python -m pip install -e ".[dev]"` - installed CivicAccess with CivicCore v1.2.0 wheel.
- `python -m ruff check .` - passed.
- `python -m pytest -q` - 18 passed.
- `bash scripts/verify-release.sh` - PASSED; 18 passed, 1 pytest-asyncio deprecation warning, ruff passed, artifacts built.

## Escalation recommendation

No escalation needed for this slice.
