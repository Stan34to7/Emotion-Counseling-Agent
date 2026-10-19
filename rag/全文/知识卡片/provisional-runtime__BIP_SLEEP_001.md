# BIP_SLEEP_001 · Decreased need for sleep vs insomnia

来源文件：`knowledge-cards/provisional-runtime/BIP_SLEEP_001.yaml`

```yaml
id: BIP_SLEEP_001
type: DIFFERENTIAL
title: Decreased need for sleep vs insomnia
clinical_claim: Decreased need for sleep in mania/hypomania is distinct from insomnia (wanting sleep but
  unable).
applies_to:
- BIP
phenomena:
- reduced_sleep_duration
- decreased_need_for_sleep
- insomnia
supports:
- decreased_need_for_sleep_if_low_sleep_need_with_energy
does_not_establish:
- manic_episode
- bipolar_disorder
alternative_explanations:
- insomnia
- voluntary_sleep_restriction
- substance_effect
- circadian_disruption
counterevidence:
- strong_daytime_sleepiness
- desire_to_sleep_but_inability
confounds: []
required_qualifiers:
- onset
- duration
- frequency
- severity
- context
- impairment
candidate_probes:
- QB-BIP-SLEEP-NEED-01
next_if_positive:
- assess_energy
- assess_mood_change
- assess_goal_directed_activity
- assess_impulsivity
- assess_substance_medication
next_if_negative:
- assess_insomnia_pattern
- assess_mood_anxiety_context
sources:
- source_id: who-icd11-cddr-2024
  locator: Manic episode essential features — decreased need for sleep distinct from insomnia
  claim_id: CLM-BIP-SLEEP-DISC
provenance:
  extraction_method: official_guideline_or_manual_paraphrase
  paraphrased: true
  source_verified: true
  structure_verified: true
review:
  clinical_reviewed: false
  expert_review: PENDING_EXTERNAL
  source_verified: true
  structure_verified: true
  expert_reviewed: false
high_stakes: true
skill_promotion:
  allowed: true
  runtime_permission: PROVISIONAL_RUNTIME
  gate_reason: semantic_source_audit_pass; expert review pending
  status: IMPLEMENTED_PENDING_EXPERT_REVIEW
audit:
  decision: KEEP
  reason: strong direct CDDR wording
verification:
  source_verified: true
  structure_verified: true
  expert_reviewed: false
runtime_permission: PROVISIONAL_RUNTIME
```
