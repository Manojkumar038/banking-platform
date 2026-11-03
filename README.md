# Digital Banking Platform

A synthetic engineering-intelligence demo repository for tracking Jira work items, Git history, pull requests, CI runs, releases and deployments across a six-month banking-platform delivery.

> **Important:** This repository is a demonstration. It is not a production banking application. It does not connect to banks, process real payments, or contain real customer information. All account, transaction, developer and historical engineering data must be synthetic.

## Product scope

- **F1 — Authentication & Security:** registration, login, password reset, MFA, session expiry.
- **F2 — Account & Beneficiary Management:** account overview, transaction history, profile updates, beneficiary management.
- **F3 — Payments, Transfers & Notifications:** simulated UPI, IMPS, NEFT and RTGS transfers, receipts and alerts.

## Technology target

- Java 21, Spring Boot and Maven
- React
- PostgreSQL
- JUnit 5 and Mockito
- GitHub Actions and Docker
- AWS EKS deployment model (demonstration only)

## Team scenario

Six synthetic contributors: two backend engineers, two frontend engineers, one QA engineer and one DevOps engineer. The planned historical scenario spans 12 two-week sprints from 5 January 2026 through 26 June 2026.

## Repository map

- `backend/` — Java/Spring Boot starter and synthetic backend fixtures
- `frontend/` — React starter and synthetic UI fixtures
- `database/` — PostgreSQL schema fixtures
- `tests/` — harmless validation tests and sample test data
- `docs/` — architecture, Jira mapping, metric definitions and data provenance
- `engineering-data/` — synthetic six-month Jira/GitHub event dataset
- `.github/workflows/` — lightweight CI validation workflow

## Traceability conventions

- Epic: `EPIC-100`
- Features: `F1`, `F2`, `F3`
- Stories: `US101`–`US118`
- Branches: `feature/F1-auth-security`, `feature/F2-account-beneficiaries`, `feature/F3-payments-notifications`
- Commit subjects should include a story or feature key, for example `[US101] Add registration validation fixture`.
- PR titles and bodies should reference their Jira keys.

## Historical event integrity

Git author and committer dates can be set for synthetic commits. GitHub PR creation, review, Actions-run and deployment timestamps are created by GitHub when those actions happen; normal GitHub APIs do not allow us to backdate those events. Historical simulated PR, CI and deployment records therefore live in `engineering-data/` and carry `data_source: synthetic`. Live events collected from GitHub must carry `data_source: actual`. Never combine the two without retaining provenance.

## Local setup

The backend and frontend folders begin as scaffolding. Follow the respective README files before installing or running either component. No secrets are required for the starter CI workflow.
