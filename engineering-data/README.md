# Synthetic Engineering Intelligence Dataset

**All records in this directory are synthetic simulation fixtures.** They are not imported from Jira or GitHub and do not correspond to real platform events.

## Scenario

- Repository target: `Manojkumar038/banking-platform`
- Period: 5 January 2026 to 26 June 2026
- Delivery cadence: 12 two-week sprints, plus final closeout/hotfix activity through 26 June
- Team: 6 synthetic contributors (2 backend, 2 frontend, 1 QA, 1 DevOps)
- Work: 1 epic, 3 features and 18 user stories

## Fixture volumes

| File | Records | Description |
|---|---:|---|
| `jira_work_items.csv.gz` | 18 | Synthetic Jira-like user stories |
| `developers.csv` | 6 | Synthetic contributor roster |
| `sprint_calendar.csv` | 12 | Two-week sprint calendar |
| `branches.csv.gz` | 67 | Synthetic branch inventory |
| `commits.csv.gz` | 378 | Synthetic commit records |
| `pull_requests.csv.gz` | 60 | 55 merged, 5 closed without merge |
| `ci_workflow_runs.csv.gz` | 90 | 55 successes, 34 failures, 1 cancellation |
| `deployments.csv.gz` | 30 | 23 successes, 6 failures, 1 rollback |
| `releases.csv` | 5 | Synthetic release records |

The CSV files are gzip-compressed. Pandas can load them directly with `pandas.read_csv("file.csv.gz")`; the standard-library loader in this folder provides a count and relationship check.

## Provenance rules

Every row has `Data_Source=synthetic`. IDs prefixed with `SIM-` are internal simulation identifiers, not GitHub or Jira IDs. GitHub-specific identifiers, URLs and commit SHAs are deliberately absent. Do not call GitHub APIs with these fixture identifiers or represent these records as actual repository commits, pull requests, Actions runs, releases or deployments.

Actual platform data collected later must be stored separately or carry `Data_Source=actual`, genuine platform IDs/URLs and platform timestamps. Never overwrite provenance when joining datasets.

## Timeline and metric integrity

- Synthetic commits precede their linked synthetic PR creation times.
- Merged PR timestamps follow PR creation; rejected PRs have blank `Merged_At` and populated `Closed_At`.
- CI runs are associated with known synthetic PRs; reruns follow initial failures.
- Deployment completion follows deployment start.
- Feature lead time uses first feature-linked commit to first successful `PROD` deployment.
- PR cycle time uses PR creation to merge; rejected PRs are excluded.
- CI and deployment metrics must declare their numerator, denominator and treatment of cancellations/rollbacks.
- Missing timestamps remain missing; do not infer them.

## Jira mapping

- Epic: `EPIC-100`
- Features: `F1` Authentication & Security; `F2` Account & Beneficiary Management; `F3` Payments, Transfers & Notifications
- User stories: `US101`–`US118`
- UPI, IMPS, NEFT and RTGS flows are simulated only.

See `DATA_DICTIONARY.md` and `../docs/metric-definitions.md`.
