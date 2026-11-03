# Architecture overview

## Logical components

1. React client — demo user interface.
2. Spring Boot API — domain and application services.
3. PostgreSQL — synthetic demo account and transfer records.
4. GitHub Actions — build and validation automation.
5. Docker / AWS EKS — target deployment model; no live cluster is configured by this repository.

## Feature boundaries

- F1 Authentication & Security
- F2 Account & Beneficiary Management
- F3 Payments, Transfers & Notifications

## Non-goals

No real payment gateway, banking core, identity provider, real secrets, or customer records are integrated. All transfer rails are simulated.
