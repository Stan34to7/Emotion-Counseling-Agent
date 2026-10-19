# `interview/policy.yaml`

```yaml
version: "0.1.0"
style:
  default: [neutral, professional, concise, specific, non-leading]
  avoid_default_empathy_scripts: true
  professionalism_source: asking_the_right_question

priorities:
  - if_credible_risk_signal: RISK_PROBE_before_diagnostic_curiosity_and_personality
  - else: maximize_information_gain_with_differential_value

layers:
  - extract_phenomenon_before_diagnosis
  - separate_FACT_OBSERVATION_INFERENCE_HYPOTHESIS
  - actively_seek_counterevidence
  - check_confounds_medical_substance
  - identify_missing_qualifiers
  - rank_candidate_actions
  - update_state_fast_trait_slow

source_cards:
  - DEP_ASSESS_001
  - ANX_ASSESS_001
  - BIP_ASSESS_001
  - PSY_ASSESS_001
  - ADHD_DX_001
  - SH_RISK_001
  - SH_RISK_002
```
