# CivicAccess Standalone Gate Walkthrough - 2026-06-06

Scope: CivicAccess v0.2.0 standalone readiness candidate after local persistence, staff workspace, records-export contract, and CivicSuite installer pin work.

Runtime:
- Service: `uvicorn civicaccess.main:app --host 127.0.0.1 --port 18101`
- Data: fresh local SQLite database through `CIVICACCESS_DATA_DIR`
- Browser: Playwright Chromium, desktop 1440x1000 and mobile 390x900
- Evidence file: `docs/qa/civicaccess-standalone-gate-2026-06-06/walkthrough-evidence.json`

## Routes

- `/civicaccess`: 200, title `CivicAccess Public Accessibility Support`
- `/civicaccess/staff`: 200, title `CivicAccess Staff Workspace`
- `/civicaccess/staff` mobile viewport: 200

## Workflows

### Public Accessibility Review

Action: Filled notice title/text, marked images as having alt text, clicked `Run review`.

Result: UI reached final state `Sample checks passed`, with staff-review and preservation next steps displayed. API-backed review persisted to the local review database.

### Staff Review Queue

Action: Opened staff workspace.

Result: Readiness card displayed `Ready`; contracts card displayed:
- `civicaccess.publication_accessibility_review.v1`
- `civicaccess.records_export.v1`

### Save Review

Action: Filled staff publication title/text, marked images as having alt text, clicked `Save review`.

Result: UI displayed `Review saved` with the generated review id and `passes-sample-checks`; review appeared in the saved review queue.

### Records Export

Action: Clicked `Export for records` on a saved review.

Result: UI displayed `Records export ready` with `civicrecords-ai: checklist-created` and the retention note. API evidence confirms endpoint-level `status=records-export-ready`, `target_module=civicrecords-ai`.

## API Cross-Check

`/api/v1/civicaccess/readiness` returned:
- `ready=true`
- `schema_ready=true`
- `review_database_configured=true`
- expected schema version `2026-06-05-001`

`/api/v1/civicaccess/integration-contracts` returned both required contracts and downstream preparation for CivicZone, CivicPlan, CivicPermit, CivicInspect, CivicGrants, and CivicProcure.

`/api/v1/civicaccess/reviews` returned the saved reviews created by the browser flow.

## Visual Check

Captured:
- `public-desktop.png`
- `staff-initial-desktop.png`
- `staff-after-export-desktop.png`
- `staff-mobile.png`

No console errors were captured. Desktop and mobile layouts are usable; controls remain visible and readable, and the mobile layout stacks panels without overlap.

## Findings

Rollup: 0 Blocker / 0 Critical / 0 Major / 0 Minor / 0 Nit.

No walkthrough findings remain for this CivicAccess standalone slice.
