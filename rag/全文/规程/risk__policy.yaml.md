# `risk/policy.yaml`

```yaml
version: "0.1.0"
priority: |
  risk assessment priority > diagnostic curiosity > personality exploration
architecture:
  model: needs_and_safety_focused_risk_formulation
  forbid:
    - predictive_risk_tools_for_future_suicide_or_repetition  # NG225 1.6.1
    - risk_tools_to_decide_treatment_or_discharge            # NG225 1.6.2
    - global_low_medium_high_to_predict                     # NG225 1.6.3
    - global_low_medium_high_to_decide_treatment_discharge  # NG225 1.6.4
  require:
    - focus_on_needs_and_immediate_long_term_safety         # NG225 1.6.5
    - risk_formulation_as_part_of_psychosocial_assessment   # NG225 1.6.6
explore_when_signal:
  - current_thoughts
  - intent
  - planning_preparation_where_relevant
  - recent_behavior
  - access_opportunity_where_relevant
  - dynamic_stressors
  - protective_factors
  - support
  - immediate_safety
  - clinical_formulation
source_cards: [SH_RISK_001, SH_RISK_002]
claim_ids: [CLM-SH-NO-RISK-SCALE-PREDICT, CLM-SH-NO-LMH-STRATIFICATION]
expert_review: PENDING_EXTERNAL
```
