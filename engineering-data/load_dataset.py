"""Load and validate the synthetic Engineering Intelligence fixtures.

Run from the repository root:
    python engineering-data/load_dataset.py

The .csv.gz files are regular gzip-compressed CSVs. No third-party packages are needed.
"""
from __future__ import annotations

import csv
import gzip
from datetime import datetime
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent
TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S"


def read_csv(name: str) -> list[dict[str, str]]:
    path = DATA_DIR / name
    opener = gzip.open if path.suffix == ".gz" else open
    with opener(path, "rt", encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream))


def parse_timestamp(value: str) -> datetime:
    return datetime.strptime(value, TIMESTAMP_FORMAT)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def main() -> None:
    datasets = {
        "jira_work_items": read_csv("jira_work_items.csv.gz"),
        "developers": read_csv("developers.csv"),
        "sprints": read_csv("sprint_calendar.csv"),
        "branches": read_csv("branches.csv.gz"),
        "commits": read_csv("commits.csv.gz"),
        "pull_requests": read_csv("pull_requests.csv.gz"),
        "ci_runs": read_csv("ci_workflow_runs.csv.gz"),
        "deployments": read_csv("deployments.csv.gz"),
        "releases": read_csv("releases.csv"),
    }
    expected = {
        "jira_work_items": 18, "developers": 6, "sprints": 12,
        "branches": 67, "commits": 378, "pull_requests": 60,
        "ci_runs": 90, "deployments": 30, "releases": 5,
    }
    for name, count in expected.items():
        require(len(datasets[name]) == count,
                f"{name}: expected {count} records, found {len(datasets[name])}")

    all_rows = [row for rows in datasets.values() for row in rows]
    require(all(row.get("Data_Source") == "synthetic" for row in all_rows),
            "Every fixture row must have Data_Source=synthetic")

    prs = {row["Pull_Request_ID"]: row for row in datasets["pull_requests"]}
    story_ids = {row["User_Story_ID"] for row in datasets["jira_work_items"]}
    require(len(prs) == 60, "Synthetic PR IDs must be unique")

    for row in datasets["commits"]:
        require(row["Pull_Request_ID"] in prs,
                f"Unknown synthetic PR link: {row['Pull_Request_ID']}")
        require(row["User_Story_ID"] in story_ids,
                f"Unknown story link: {row['User_Story_ID']}")
        pr = prs[row["Pull_Request_ID"]]
        require(parse_timestamp(row["Commit_Date"]) < parse_timestamp(pr["Created_At"]),
                f"Commit must precede PR creation: {row['Commit_ID']}")

    merged = [p for p in prs.values() if p["PR_Status"] == "Merged"]
    rejected = [p for p in prs.values() if p["PR_Status"] == "Closed - Rejected"]
    require(len(merged) == 55 and len(rejected) == 5,
            "PR status distribution must be 55 merged / 5 closed without merge")
    for pr in merged:
        require(pr["Merged_At"] and pr["Closed_At"] == "",
                f"Merged PR timestamps inconsistent: {pr['Pull_Request_ID']}")
        require(parse_timestamp(pr["Merged_At"]) > parse_timestamp(pr["Created_At"]),
                f"PR merge must follow creation: {pr['Pull_Request_ID']}")
    for pr in rejected:
        require(pr["Merged_At"] == "" and pr["Closed_At"],
                f"Rejected PR must not have a merge timestamp: {pr['Pull_Request_ID']}")

    for run in datasets["ci_runs"]:
        require(run["Pull_Request_ID"] in prs, f"Unknown PR for CI run: {run['Workflow_Run_ID']}")
        pr = prs[run["Pull_Request_ID"]]
        require(parse_timestamp(run["Started_At"]) >= parse_timestamp(pr["Created_At"]),
                f"CI run must not precede PR creation: {run['Workflow_Run_ID']}")

    conclusions = {}
    for row in datasets["ci_runs"]:
        conclusions[row["Conclusion"]] = conclusions.get(row["Conclusion"], 0) + 1
    require(conclusions == {"failure": 34, "success": 55, "cancelled": 1},
            f"Unexpected CI conclusions: {conclusions}")

    for deployment in datasets["deployments"]:
        require(parse_timestamp(deployment["Completed_At"]) > parse_timestamp(deployment["Started_At"]),
                f"Deployment completion must follow start: {deployment['Deployment_ID']}")
    prod_attempts = [d for d in datasets["deployments"] if d["Environment"] == "PROD"]
    require(len(prod_attempts) == 12, "Expected 12 synthetic production deployment attempts")

    merged_story_ids = {p["User_Story_ID"] for p in merged}
    committed_story_ids = {c["User_Story_ID"] for c in datasets["commits"]}
    require(story_ids <= merged_story_ids, "Every story must have at least one merged PR")
    require(story_ids <= committed_story_ids, "Every story must have at least one linked commit")

    print("Synthetic dataset validation passed.")
    for name, rows in datasets.items():
        print(f"{name}: {len(rows)} records")
    print(f"CI conclusions: {conclusions}")
    print(f"Production deployment attempts: {len(prod_attempts)}")


if __name__ == "__main__":
    main()
