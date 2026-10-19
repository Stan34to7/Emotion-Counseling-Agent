# `personality/state-trait-rules.yaml`

```yaml
version: "0.1.0"
ladder:
  - STATE
  - EPISODE
  - PATTERN
  - TRAIT
  - STRUCTURAL_PERSONALITY
promotion_requirements_for_trait:
  - repetition
  - cross_context_consistency
  - temporal_stability
  - behavioral_evidence
  - counterevidence_reviewed
  - exceptions_noted
  - state_confounds_ruled_out_or_accounted
hard_rule_card: STATE_TRAIT_001
examples:
  - from: "今天不想社交"
    allow: "state.social_engagement_down"
    forbid: "trait.social_detachment"
```
