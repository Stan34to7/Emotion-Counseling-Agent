# `personality/construct-inference-matrix.yaml`

```yaml
version: 0.1.0
status: IMPLEMENTED_PENDING_EXPERT_REVIEW
promotion_policy:
  STATE: allowed_from_single_clear_report_with_low_confidence
  EPISODE: requires_time_bound_recurrence
  PATTERN: requires_cross_context_repetition
  TRAIT: requires_temporal_stability_plus_aggregation_evidence
  STRUCTURAL_PERSONALITY: above_trait_plus_expert_threshold
sources_for_promotion_policy:
- fleeson-gallagher-2009-esm
- bleidorn-2022-stability-meta
- STATE_TRAIT_001
constructs:
- id: self_esteem
  conversational_inference: weak_only
  flag: null
- id: self_efficacy
  conversational_inference: weak_only
  flag: null
- id: agency
  conversational_inference: weak_only
  flag: INSUFFICIENT_EVIDENCE_FOR_CONVERSATIONAL_INFERENCE
- id: autonomy
  conversational_inference: weak_only
  flag: INSUFFICIENT_EVIDENCE_FOR_CONVERSATIONAL_INFERENCE
- id: need_for_control
  conversational_inference: weak_only
  flag: null
- id: reward_sensitivity
  conversational_inference: weak_only
  flag: null
- id: threat_sensitivity
  conversational_inference: weak_only
  flag: null
- id: achievement_motivation
  conversational_inference: weak_only
  flag: INSUFFICIENT_EVIDENCE_FOR_CONVERSATIONAL_INFERENCE
- id: status_motivation
  conversational_inference: weak_only
  flag: INSUFFICIENT_EVIDENCE_FOR_CONVERSATIONAL_INFERENCE
- id: affiliation_motivation
  conversational_inference: weak_only
  flag: null
- id: trust
  conversational_inference: weak_only
  flag: null
- id: intimacy
  conversational_inference: weak_only
  flag: INSUFFICIENT_EVIDENCE_FOR_CONVERSATIONAL_INFERENCE
- id: dependency
  conversational_inference: weak_only
  flag: null
- id: rejection_sensitivity
  conversational_inference: weak_only
  flag: null
- id: interpersonal_conflict_style
  conversational_inference: weak_only
  flag: INSUFFICIENT_EVIDENCE_FOR_CONVERSATIONAL_INFERENCE
- id: emotion_regulation
  conversational_inference: weak_only
  flag: null
- id: rumination
  conversational_inference: weak_only
  flag: null
- id: perfectionism
  conversational_inference: weak_only
  flag: null
- id: cognitive_flexibility
  conversational_inference: insufficient
  flag: INSUFFICIENT_EVIDENCE_FOR_CONVERSATIONAL_INFERENCE
- id: identity_coherence
  conversational_inference: insufficient
  flag: INSUFFICIENT_EVIDENCE_FOR_CONVERSATIONAL_INFERENCE
- id: values
  conversational_inference: insufficient
  flag: INSUFFICIENT_EVIDENCE_FOR_CONVERSATIONAL_INFERENCE
counts:
  total: 21
  weak_only: 18
  insufficient: 9
  reliable_strong: 0
conclusion: 'No functional personality construct in this set is validated for strong trait lock from short
  natural-language chat. Best available: weak state/pattern hypotheses with mandatory counterevidence
  and state-confound checks.'
```
