CivicAccess
===========

CivicAccess is the CivicSuite module for accessibility, plain-language, multilingual, and ADA Title II review-support workflows.

Current state: v0.4.0 standalone readiness candidate. This repo contains a deterministic FastAPI package aligned to the published CivicCore v1.2.0 release wheel, health/root endpoints, readiness gates, WCAG-aligned review support, database-backed review records that default to the shared CivicCore PostgreSQL (with a SQLite dev fallback), accessible form planning, accessible publishing workflow checks, plain-language rewrites, multilingual draft variants, ADA Title II review-support packages, tagged-PDF expectations, records-ready export checklists, a stateless public accessibility checker at /civicaccess, and a trusted-write-token-guarded staff persistence/export surface with persisted audit events. The previous v1.0.0 release was published in error and is superseded by this honest sub-1.0.0 label.

CivicAccess does not provide legal advice, certified ADA compliance, official translation certification, live LLM calls, or final publication approval. City staff, ADA coordinators, translators, and qualified reviewers remain responsible for publication decisions.

Run:

python -m pip install -e ".[dev]"
python -m pytest -q
bash scripts/verify-release.sh
