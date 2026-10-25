# STATE_TRAIT_001 · Single utterance cannot promote trait

来源文件：`knowledge-cards/provisional-runtime/STATE_TRAIT_001.yaml`

```yaml
id: STATE_TRAIT_001
type: STATE_TRAIT_RULE
title: Single utterance cannot promote trait
clinical_claim: A single-session state report must not be promoted to trait/structural personality without
  evidence of temporal stability and cross-context aggregation; personality literature shows traits relate
  to aggregated behavioral distributions, not single occasions (Fleeson & Gallagher, 2009 experience-sampling
  meta-analysis; longitudinal rank-order stability meta-analyses).
applies_to:
- personality
phenomena: []
supports: []
does_not_establish:
- any_trait_from_one_utterance
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
- source_id: fleeson-gallagher-2009-esm
  locator: PMC2791901 — trait standing predicts mean behavioral manifestation across situations (r>.40)
  claim_id: CLM-STATE-TRAIT-AGGREGATION
- source_id: bleidorn-2022-stability-meta
  locator: Psychol Bull meta-analysis — rank-order trait stability increases then plateaus; facets/maladaptive
    less stable
  claim_id: CLM-STATE-TRAIT-AGGREGATION
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
high_stakes: false
skill_promotion:
  allowed: true
  runtime_permission: PROVISIONAL_RUNTIME
  gate_reason: source_audit_pass_with_narrowing; expert review pending
  status: IMPLEMENTED_PENDING_EXPERT_REVIEW
audit:
  decision: KEEP_NARROWED
  reason: re-sourced to personality meta-analytic literature; removed fake NG222 causal citation as sole
    basis
verification:
  source_verified: true
  structure_verified: true
  expert_reviewed: false
runtime_permission: PROVISIONAL_RUNTIME
```
