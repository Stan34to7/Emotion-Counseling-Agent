# BIP_SLEEP_002 · Short sleep insufficient for mania

来源文件：`knowledge-cards/provisional-runtime/BIP_SLEEP_002.yaml`

```yaml
id: BIP_SLEEP_002
type: INSUFFICIENT_FOR
title: Short sleep insufficient for mania
clinical_claim: Reduced sleep duration alone is insufficient for mania/hypomania without sleep-need phenomenology
  and accompanying mood/activation features.
applies_to:
- BIP
phenomena:
- reduced_sleep_duration
supports: []
does_not_establish:
- manic_episode
- hypomanic_episode
- bipolar_disorder
alternative_explanations: []
counterevidence: []
confounds: []
required_qualifiers:
- onset
- duration
- frequency
- severity
- context
- impairment
candidate_probes: []
next_if_positive: []
next_if_negative: []
sources:
- source_id: who-icd11-cddr-2024
  locator: Manic episode essential (required) features — multi-feature structure
  claim_id: CLM-BIP-SHORT-SLEEP-INSUFFICIENT
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
  reason: derived from multi-feature essential structure — not single sentence
verification:
  source_verified: true
  structure_verified: true
  expert_reviewed: false
runtime_permission: PROVISIONAL_RUNTIME
```
