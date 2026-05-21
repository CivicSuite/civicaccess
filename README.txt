CivicAccess
===========

CivicAccess is the CivicSuite module for accessibility, plain-language, multilingual, and ADA Title II review-support workflows.

Current state: v1.0.0 public-use support release. This repo ships a FastAPI package, health/root endpoints, deterministic WCAG-aligned review support, optional database-backed review records via CIVICACCESS_REVIEW_DB_URL, accessible form planning, accessible publishing workflow checks, plain-language rewrites, multilingual draft variants, ADA Title II review-support packages, tagged-PDF expectations, records-ready export checklists, a functional public UI at /civicaccess, and civiccore==1.1.0 dependency alignment.

CivicAccess does not provide legal advice, certified ADA compliance, official translation certification, live LLM calls, or final publication approval. City staff, ADA coordinators, translators, and qualified reviewers remain responsible for publication decisions.

Run:

python -m pip install -e ".[dev]"
python -m pytest -q
bash scripts/verify-release.sh
