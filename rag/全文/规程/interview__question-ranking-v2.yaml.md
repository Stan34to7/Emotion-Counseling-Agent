# `interview/question-ranking-v2.yaml`

```yaml
version: "0.2.0"
status: IMPLEMENTED_PENDING_EXPERT_REVIEW

priority_order:
  - SAFETY
  - CRITICAL_PREREQUISITE
  - CONFOUND_EXCLUSION
  - MAJOR_CONTRADICTION
  - HIGH_VALUE_DIFFERENTIAL
  - FUNCTIONAL_IMPACT
  - TIMELINE_IMPORTANCE
  - MODEL_UNCERTAINTY_REDUCTION
  - PERSONALITY_REFINEMENT

bands: [critical, high, medium, low, defer]

penalties:
  - REDUNDANCY
  - LEADINGNESS
  - PATIENT_BURDEN
  - INFORMATION_SATURATION

actions_beyond_question:
  - DEFER
  - CONTINUE_TOPIC
  - SUMMARIZE_VERIFY

semantic_action_fields:
  - action_type
  - target_constructs
  - information_objective
```
