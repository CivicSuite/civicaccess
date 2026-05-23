# CivicAccess Depth Probe Progress - 2026-05-23

## Verdict

Clearly NEEDS-WORK. Default OUT of city-core.

CivicAccess does not pass the full city-core public-use gate. This probe did not
attempt a v1 release and did not change product code.

## Evidence Read

- Live main checked at `ad36612f` (`fix: demote civicaccess false v1 release truth (#7)`).
- `README.md` and `USER-MANUAL.md` describe CivicAccess as `v0.2.0`
  corrective demotion state.
- `README.md` explicitly says CivicAccess is not finished, shipping,
  city-ready, product-ready, or public-use ready.
- `README.md` explicitly says CivicAccess has no real AI layer, no real
  municipal data/search layer, no production-grade frontend, and no independent
  Section 2 public-use gate sign-off.

## Local Verification

Global-environment tests:

- `python -m pytest -q` ran 17 tests.
- Result: 16 passed, 1 failed.
- Failure: `tests/test_runtime_foundation.py::test_health_endpoint_reports_versions`
  expected `civiccore_version == "1.1.0"` but imported `1.2.0` from the global
  environment.

Clean install probe:

- Created `.tmp-probe-venv`.
- `python -m pip install -e ".[dev]"` failed because `pyproject.toml` pins
  bare `civiccore==1.1.0`.
- `civiccore` is not available from PyPI under that name/version in the clean
  resolver path, so CivicAccess is not cleanly installable from its own docs as
  currently written.
- `scripts/verify-release.sh` could not run in the clean venv after that failed
  install because the dev dependencies were not installed.

## Gate Findings

1. **Installable + runnable: FAIL.**
   The repo pins `civiccore==1.1.0` instead of the release-asset URL convention
   used by other CivicSuite modules. Clean install fails.

2. **Authz / staff-public boundary: FAIL / absent.**
   The exposed routes are public deterministic support endpoints. No real staff
   auth boundary was found in the initial source read.

3. **Audit logging: FAIL / absent.**
   No module-level audit log path was found in the initial source read.

4. **Backup / restore: FAIL / absent.**
   No backup/restore proof or module operational lifecycle was found.

5. **Installer integration: FAIL / unproven.**
   No city-core installer packaging proof exists for CivicAccess.

6. **Browser-verified UX: NOT CURRENT.**
   Historical browser QA files exist, including mistaken v1 evidence, but this
   probe did not produce current-session desktop/mobile browser evidence against
   a running installed stack.

7. **Product substance: PARTIAL.**
   The module has deterministic accessibility, plain-language, multilingual,
   ADA-support, tagged-PDF, export, and optional review persistence workflows.
   It does not have a real AI layer, real municipal data/search, production
   frontend, or public-use gate evidence.

## Recommendation

Keep CivicAccess OUT of city-core for this sprint.

Handle CivicAccess in the caboose as a demoted module unless the owner
separately authorizes a full CivicAccess finish sprint. If it is revisited, the
first required fix is to make the package cleanly installable by replacing the
bare CivicCore dependency with the proper release-asset URL pin, then build the
missing authz, audit logging, backup/restore, installer, and browser-QA evidence.

