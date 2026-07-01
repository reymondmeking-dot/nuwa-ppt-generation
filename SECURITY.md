# Security Policy

## Supported versions

Only the `main` branch of this repository is actively maintained. Security fixes are applied to `main`; older tagged snapshots are not backported.

## Secrets

Do not commit API keys, provider tokens, cookies, SSH keys, or generated `.env` files.

The repository may mention environment variable names such as `GEMINI_API_KEY` or `OPENAI_API_KEY` in documentation, but real values must stay outside git. If you accidentally push a secret:

1. Rotate the credential at the provider immediately.
2. Remove it from history (e.g. `git filter-repo`) and force-push if the repository is private, or contact the maintainer for coordinated cleanup if it is public.

## Reporting a vulnerability

If you discover a security issue, please **do not open a public GitHub issue**. Instead, report it privately:

- Open a GitHub **Security Advisory** on this repository (`Security` tab → `Report a vulnerability`), **or**
- Contact the maintainer via GitHub (`@reymondmeking-dot`) with a private channel request.

Please include:

- A description of the issue and its impact.
- Steps to reproduce (proof-of-concept preferred).
- Affected files, commits, or components.
- Your suggested fix, if any.

## Disclosure process

- We aim to acknowledge new reports **within 5 business days**.
- We aim to publish a fix or mitigation **within 30 days** for confirmed high-severity issues, and to coordinate a public disclosure with the reporter.
- Do not publish exploitable credentials or user data in public issues, PRs, or discussions during the coordination window.

## Scope

In scope:

- Code in this repository (`skills/`, demo scripts, docs that ship executable snippets).
- Documentation that could mislead a user into insecure configuration.

Out of scope:

- Vulnerabilities in third-party dependencies (please report those upstream).
- Issues in unrelated forks or downstream products.
