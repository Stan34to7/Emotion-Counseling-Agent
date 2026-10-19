# `ontology/relations.yaml`

```yaml
relation_types:
- is_a
- part_of
- associated_with
- supports
- weakly_supports
- contradicts
- insufficient_for
- requires
- differentiate_from
- possible_explanation
- confounded_by
- rule_out_if
- probe_with
- follow_up_if_positive
- follow_up_if_negative
- temporally_precedes
- state_expression_of
- trait_expression_of
- maintained_by
- protective_against
edges:
- from: reduced_sleep_duration
  rel: insufficient_for
  to: manic_episode
  card: BIP_SLEEP_002
- from: reduced_sleep_duration
  rel: differentiate_from
  to: decreased_need_for_sleep
  card: BIP_SLEEP_001
- from: reduced_sleep_duration
  rel: probe_with
  to: QB-BIP-SLEEP-NEED-01
  card: BIP_SLEEP_001
- from: unusual_belief
  rel: insufficient_for
  to: delusion
  card: PSY_BELIEF_001
- from: poor_concentration
  rel: insufficient_for
  to: adhd
  card: ADHD_CONC_001
- from: low_mood
  rel: insufficient_for
  to: depressive_disorder
  card: DEP_MOOD_001
- from: reduced_social_engagement
  rel: insufficient_for
  to: avoidant_personality_disorder
  card: SOC_TRAIT_001
- from: rdoc_construct
  rel: insufficient_for
  to: any_icd_diagnosis
  card: RDOC_LIM_001
```
