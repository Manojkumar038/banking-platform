# Digital Banking Platform

Synthetic engineering-intelligence demonstration repository for a digital banking product scenario.

> This is not a production banking application. It does not connect to banks, move money, or contain real customer data.

## Product scope

- **F1 — Authentication & Security:** registration, login, password reset, MFA and session expiry.
- **F2 — Account & Beneficiary Management:** account overview, transaction history, profile updates and beneficiary management.
- **F3 — Payments, Transfers & Notifications:** simulated UPI, IMPS, NEFT and RTGS transfers, receipts and alerts.

## Technology target

Java 21, Spring Boot, Maven, React, PostgreSQL, JUnit 5, Mockito, GitHub Actions, Docker and an AWS EKS deployment model (simulated).

## Repository layout

- `backend/`: Java/Spring Boot scaffold
- `frontend/`: React scaffold
- `database/`: PostgreSQL schema fixtures
- `tests/`: validation and synthetic test fixtures
- `docs/`: architecture, Jira traceability, metric definitions and provenance policy
- `engineering-data/`: synthetic six-month delivery history and loader

## Work-item conventions

Epic `EPIC-100`; features `F1`, `F2`, `F3`; stories `US101`–`US118`. Branch names, commit messages and PR titles in the synthetic scenario carry these IDs for traceability.

## Historical data is synthetic

The files in `engineering-data/` are simulation fixtures, not actual GitHub or Jira events. GitHub PRs, reviews, Actions runs and deployments created in the real platform receive current platform timestamps. Synthetic history is separately stored and tagged `Data_Source=synthetic`; live API-collected data must be tagged `Data_Source=actual`. See `engineering-data/README.md` before analyzing metrics.

Run `python engineering-data/load_dataset.py` to validate and inspect the compressed CSV fixtures.
