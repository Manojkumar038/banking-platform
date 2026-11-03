# Engineering data dictionary

| File | Grain | Key fields | Notes |
|---|---|---|---|
| `jira_work_items.csv.gz` | One story | `User_Story_ID`, `Feature_ID` | Synthetic Jira-like records; real Jira issue key is intentionally absent. |
| `developers.csv` | One contributor | `Developer_ID` | Synthetic roster; not actual GitHub usernames. |
| `sprint_calendar.csv` | One sprint | `Sprint_ID` | Twelve two-week sprint windows. |
| `branches.csv.gz` | One branch fixture | `Branch_Name` | Not actual Git refs. |
| `commits.csv.gz` | One commit fixture | `Commit_ID`, `Pull_Request_ID` | Not actual Git commits; no Git SHA is provided. |
| `pull_requests.csv.gz` | One PR fixture | `Pull_Request_ID` | Internal simulation key; GitHub number and URL are blank. |
| `ci_workflow_runs.csv.gz` | One workflow-run fixture | `Workflow_Run_ID`, `Pull_Request_ID` | Not actual GitHub Actions runs. |
| `deployments.csv.gz` | One deployment fixture | `Deployment_ID`, `Release_Version` | Not actual GitHub deployments; AWS EKS is simulated. |
| `releases.csv` | One release fixture | `Release_Version` | Not an actual GitHub Release object. |

## Shared conventions

- `Data_Source=synthetic` on every row in this folder. Future API-collected records should use `actual`.
- IDs beginning `SIM-` are internal simulation identifiers. Do not call GitHub or Jira APIs with them.
- `Pull_Request_ID` joins synthetic commits, PRs and CI runs.
- Timestamps are scenario timestamps in Asia/Kolkata (+05:30), without explicit offsets.
- Rejected PRs have blank `Merged_At` and populated `Closed_At`.
- Blank platform identifiers are deliberate. Never invent GitHub URLs, SHA values or numeric IDs.
- Gzip-compressed CSVs are readable directly by pandas.

## Metric guidance

Feature lead time: earliest story-linked commit for a feature to first successful `PROD` deployment for that feature. Story development time: earliest story-linked commit to first merged PR timestamp. PR cycle time: `Created_At` to `Merged_At`; do not compute for rejected PRs. CI reliability: successful completed runs divided by all completed runs; report cancelled runs separately unless the metric definition says otherwise. Deployment frequency and change failure rate should use `PROD` only unless explicitly stated otherwise.
