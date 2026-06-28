# Security

CivicAccess version: `0.4.0`.

CivicAccess is self-hosted municipal software. It provides advisory accessibility, plain-language, multilingual draft, and ADA Title II review-support workflows; it does not make legal, certification, translation, or publication decisions.

Persistent writes (saving reviews and records exports) require the `CIVICACCESS_TRUSTED_WRITE_TOKEN` server secret, sent by the staff surface as the `X-CivicAccess-Write-Token` header. The public surface (`/civicaccess`) analyzes content statelessly and never persists. When the write token is not configured, persistence-backed writes fail closed (HTTP 503) rather than accepting unauthenticated writes.

Report vulnerabilities privately through the CivicSuite project maintainers. Do not include secrets, resident data, or protected municipal records in public issues.
