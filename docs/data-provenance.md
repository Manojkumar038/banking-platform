# Data provenance policy

## Synthetic history

Historical simulation records are generated for testing the Engineering Intelligence Agent. They are not actual events on GitHub or Jira. Every record must include `data_source: synthetic` and retain its original simulated event timestamp.

## Actual platform events

Records collected from GitHub or Jira APIs must include `data_source: actual` and preserve the platform timestamp and source identifier.

## Combining datasets

Never overwrite provenance. Reports must show synthetic and actual counts separately. A mixed analysis must make the split explicit and must not present simulated PRs, reviews, workflow runs or deployments as real GitHub activity.
