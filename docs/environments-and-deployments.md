# GitHub Environments and deployment workflows

| Environment | Workflow | Trigger | Meaning shown in Actions |
|---|---|---|---|
| DEV | `.github/workflows/deploy-dev.yml` | Push to `main` or `promotion/dev`; manual dispatch | `Deployment triggered to DEV` |
| TEST | `.github/workflows/deploy-test.yml` | Push to `promotion/test`; manual dispatch | `Deployment triggered to TEST` |
| PROD | `.github/workflows/deploy-prod.yml` | Push to `promotion/prod`; manual dispatch | `Deployment triggered to PROD` |

Each run name includes environment, branch and source commit SHA. Job steps print the same deployment trigger and identify the source branch and SHA. Each workflow writes an execution manifest and uploads it as a run artifact.

## Promotion branches

- `promotion/dev`: triggers a DEV validation/execution record.
- `promotion/test`: triggers a TEST validation/execution record.
- `promotion/prod`: triggers a PROD validation/execution record.
- Promote only a revision that has passed the preceding environment stage.
- Configure PROD environment required reviewers and branch restrictions before treating PROD as protected.

## Current deployment limitation

The repository still has no running banking application, hosting service, container registry, AWS account/cluster connection, or deployment credentials. The current workflows validate the repository fixtures and upload a deployment manifest using the GitHub Environment. They do **not** deploy an application to a DEV, TEST or PROD runtime.

Each manifest sets `application_runtime_deployed: false` and `runtime_target: null`. These are genuine GitHub Actions executions and environment records, but they must not be counted as application deployment-frequency or change-failure events.

When a runtime is provisioned, replace the metadata-only stage with build/publish/deploy steps (for example, publish a container image and update an EKS workload). Keep environment-specific credentials in GitHub Environment secrets.
