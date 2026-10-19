# `interview/question-ranking.yaml`

```yaml
version: "0.1.0"
formula_ordinal: |
  priority ≈ information_gain + safety_priority + differential_value + prerequisite_value
             - redundancy - leadingness - unnecessary_burden
bands: [critical, high, medium, low]
rules:
  - id: RANK-RISK
    if: risk_relevant_ambiguity_or_disclosure
    then_band: critical
    action_type: RISK_PROBE
    source: SH_RISK_001
  - id: RANK-SLEEP-DISC
    if: reduced_sleep_duration_without_sleep_need_qualifier
    then_band: high
    preferred_probe: QB-BIP-SLEEP-NEED-01
    source: BIP_SLEEP_001
  - id: RANK-INSUFFICIENT
    if: phenomenon_hits_insufficient_for_library
    then_band: high
    prefer: phenomenology_or_differential_probe_not_diagnosis_label
  - id: RANK-AVOID-LEADING
    if: candidate_implies_diagnosis_in_wording
    then: demote_or_rewrite
```
