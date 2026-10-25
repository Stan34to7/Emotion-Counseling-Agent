# `personality/inference-policy.yaml`

```yaml
version: "0.1.0"
rules:
  - never_promote_trait_from_single_utterance
  - personality_pathology_threshold_higher_than_normal_traits
  - separate_disease_state_from_personality
  - chat_inference_is_not_ipip_score
  - every_construct_needs_value_confidence_stability_separately
```
