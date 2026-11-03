"""Load and validate the synthetic Engineering Intelligence fixtures.

Run from the repository root:
    python engineering-data/load_dataset.py

The .csv.gz files are regular gzip-compressed CSVs. No third-party packages are needed.
"""
from __future__ import annotations

import csv
import gzip
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent


def read_csv(name: str) -> list[dict[str, str]]:
    path = DATA_DIR / name
    opener = gzip.open if path.suffix == ".gz" else open
    with opener(path, "rt", encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream))


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
    for row in datasets["commits"] + datasets["ci_runs"]:
        require(row["Pull_Request_ID"] in prs,
                f"Unknown synthetic PR link: {row['Pull_Request_ID']}")
        require(row["User_Story_ID"] in story_ids,
                f"Unknown story link: {row['User_Story_ID']}")

    merged = [p for p in prs.values() if p["PR_Status"] == "Merged"]
    rejected = [p for p in prs.values() if p["PR_Status"] == "Closed - Rejected"]
    require(len(merged) == 55 and len(rejected) == 5,
            "PR status distribution is unexpected")
    require(all(p["Merged_At"] and p["Closed_At"] == "" for p in merged),
            "Merged PR timestamps are inconsistent")
    require(all(p["Merged_At"] == "" and p["Closed_At"] for p in rejected),
            "Rejected PR timestamps are inconsistent")

    print("Synthetic dataset validation passed.")
    for name, rows in datasets.items():
        print(f"{name}: {len(rows)} records")


if __name__ == "__main__":
    main()
