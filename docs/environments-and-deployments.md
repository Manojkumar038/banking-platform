# GitHub Environments and deployment workflows

This repository defines three GitHub Environments:

| Environment | Workflow | Trigger | Intended use |
|---|---|---|---|
| DEV | `.github/workflows/deploy-dev.yml` | Push to `main` or manual dispatch | Developer integration / early validation |
| TEST | `.github/workflows/deploy-test.yml` | Manual dispatch | QA promotion after validation |
| PROD | `.github/workflows/deploy-prod.yml` | Manual dispatch | Controlled production promotion |

`.github/workflows/initialize-environments.yml` references all three environments with `deployment: false`. On its first run, GitHub creates any missing environments without creating deployment-history records.

## Current deployment limitation

The repository does not yet contain a runnable banking application, configured hosting service, Docker registry, AWS account/cluster connection or deployment credentials. Therefore the three deployment workflows currently:

1. Check out the selected `main` revision.
2. Validate the synthetic engineering dataset.
3. Write and upload a deployment manifest.
4. Use the relevant GitHub Environment so GitHub records the workflow's environment execution.

The manifest explicitly sets `application_runtime_deployed: false`. These are real GitHub workflow and environment records, but they are **not evidence that an application was deployed to DEV, TEST or PROD**. Do not count these metadata-only records as application deployment frequency or change-failure events.

When a real runtime is provisioned, replace the metadata-only stage with the actual deployment action (for example, build/publish a container and update the relevant Kubernetes deployment). Store environment-specific credentials as GitHub Environment secrets; do not commit secrets.

## Protection settings

- DEV: restrict deployments to `main` if desired; no approval is normally needed.
- TEST: optionally restrict deployments to `main` and add QA approval.
- PROD: configure required reviewers before running the PROD workflow. Prefer a reviewer other than the workflow initiator and enable prevention of self-review where a separate reviewer is available.

GitHub automatically creates an environment the first time a workflow job references a missing environment. Such automatically created environments have no protection rules or secrets by default. Repository administrators must configure those settings separately.
