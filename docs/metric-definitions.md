# Engineering metric definitions

All metric calculations must state the source, time window, inclusion rules and missing-data treatment.

- **Feature lead time:** first feature-linked implementation commit to first successful production deployment. Keep the start/end event definition fixed across comparisons.
- **Story development time:** first story-linked commit to PR merge timestamp.
- **PR cycle time:** PR creation timestamp to merge timestamp. Unmerged or rejected PRs do not have a merge timestamp and must not be counted as merged.
- **CI reliability:** successful completed workflow runs divided by all completed workflow runs in the selected population.
- **Deployment frequency:** successful production deployments per period.
- **Change failure rate:** failed or rolled-back production deployment attempts divided by all production deployment attempts.

Do not invent missing timestamps. Exclude or report incomplete records explicitly. Do not substitute commit author date for PR creation, review, CI run or deployment event time.

Synthetic historical events and actual GitHub events must be segmented by `data_source` before calculating metrics.
