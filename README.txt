CivicAccess
===========

CivicAccess is the CivicSuite module for accessibility, plain-language, multilingual, and ADA review support.

Current state: v0.1.1 accessibility foundation release. This repo ships a FastAPI package, health/root endpoints, documentation gates, deterministic sample accessibility review, plain-language rewrite, multilingual variant, records-ready export checklist, accessible public sample UI at /civicaccess, and civiccore==0.3.0 dependency alignment. It does not ship certified ADA compliance, legal advice, live LLM calls, production translation workflows, document ingestion, or suite-wide integration APIs.

Developer quickstart:

python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
python -m pytest -q
bash scripts/verify-release.sh

Code license: Apache 2.0.
Documentation license: CC BY 4.0.
