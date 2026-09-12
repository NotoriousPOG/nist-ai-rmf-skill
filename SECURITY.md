# Security Policy

## Do not commit

- API keys, PATs, OAuth tokens, private keys, connection strings
- Filled customer assessment/inventory reports with real org data (unless explicitly redacted and approved)
- `.env` files

Assessment reports should record credential **metadata** only (name, owner, scope, expiry).

## Reporting

If you find a security issue in this repository (e.g. accidental secret exposure in history), open a private report via GitHub Security Advisories for this repo, or contact the maintainer.
