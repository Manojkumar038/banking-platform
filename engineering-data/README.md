# Engineering data fixtures

Place the synthetic six-month dataset here. Expected files include Jira work items, developers, branches, commits, pull requests, CI workflow runs, deployments and releases.

Every record must carry a provenance field (`data_source=synthetic` for generated historical data or `data_source=actual` for API-collected platform events). Synthetic platform event timestamps must never be represented as genuine GitHub/Jira event timestamps.
