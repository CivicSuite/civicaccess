# QA Deep Dive

Scope: runtime behavior, browser walkthrough, API cross-checks, local persistence, screenshots, and console/runtime errors.

## Findings

Rollup: 0 Blocker / 0 Critical / 0 Major / 0 Minor / 0 Nit.

No QA findings.

## Runtime Evidence

- Local service started on `127.0.0.1:18101`
- Fresh local SQLite data directory
- `/api/v1/civicaccess/readiness`: `ready=true`, `schema_ready=true`
- `/api/v1/civicaccess/integration-contracts`: required contracts present
- `/civicaccess`: browser status 200
- `/civicaccess/staff`: browser status 200
- Browser console: no errors captured

## Workflow Evidence

Public workflow:
- Filled public notice.
- Ran review.
- Final UI state: `Sample checks passed`.

Staff workflow:
- Readiness card loaded live ready state.
- Contract card loaded published contracts.
- Saved a review.
- Review appeared in saved queue.
- Exported the review for records.
- Final UI state: `Records export ready` with `civicrecords-ai: checklist-created`.

## Assessment

The runtime path works as a real clerk-facing slice. The UI is not merely decorative: visible controls call live endpoints, persist review records, refresh the queue, and export records packages.
