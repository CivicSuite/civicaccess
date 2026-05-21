CivicAccess
===========

CivicAccess is the CivicSuite module for accessibility, plain-language, multilingual, and ADA Title II review-support workflows.

Current state: v0.2.0 corrective demotion state. This repo contains a deterministic scaffold with a FastAPI package, health/root endpoints, WCAG-aligned review support, optional database-backed review records via CIVICACCESS_REVIEW_DB_URL, accessible form planning, accessible publishing workflow checks, plain-language rewrites, multilingual draft variants, ADA Title II review-support packages, tagged-PDF expectations, records-ready export checklists, a public UI at /civicaccess, and civiccore==1.1.0 dependency alignment. The previous v1.0.0 release was published in error and is superseded by this honest sub-1.0.0 label.

CivicAccess does not provide legal advice, certified ADA compliance, official translation certification, live LLM calls, or final publication approval. City staff, ADA coordinators, translators, and qualified reviewers remain responsible for publication decisions.

Run:

python -m pip install -e ".[dev]"
python -m pytest -q
bash scripts/verify-release.sh
