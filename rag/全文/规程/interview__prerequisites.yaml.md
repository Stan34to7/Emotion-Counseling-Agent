# `interview/prerequisites.yaml`

```yaml
version: "0.2.0"
status: IMPLEMENTED_PENDING_EXPERT_REVIEW
note: "Order constraints for clinical actions. Not disease encyclopedia."

prerequisites:
  - id: PRE-ADHD-TRAIT
    before_action_objectives: [evaluate_adhd_trait, deepen_adhd_diagnosis]
    require_unknowns_resolved_or_probed:
      - developmental_onset
      - cross_setting_persistence
      - functional_impairment_adhd
    also_screen:
      - mood_contribution
      - sleep_contribution
      - substance_medication_contribution
    knowledge_refs: [ADHD_DX_001, ADHD_CONC_001]

  - id: PRE-ANHEDONIA
    before_action_objectives: [label_global_anhedonia, deepen_depressive_anhedonia]
    require_unknowns_resolved_or_probed:
      - anhedonia_scope
      - reward_baseline
      - functional_impairment_mood
    knowledge_refs: [ANHED_SCOPE_001, DEP_ASSESS_001]

  - id: PRE-PERSONALITY-TRAIT
    before_action_objectives: [promote_trait_candidate, deepen_personality_pathology]
    require_unknowns_resolved_or_probed:
      - baseline_vs_current
      - acute_state_contamination
      - cross_context_consistency
    hard_cap: TRAIT_CANDIDATE
    knowledge_refs: [STATE_TRAIT_001, SOC_TRAIT_001]

  - id: PRE-UNUSUAL-BELIEF
    before_action_objectives: [label_delusion, deepen_psychosis_diagnosis]
    require_unknowns_resolved_or_probed:
      - belief_conviction
      - alternative_explanations
      - cultural_sharedness
      - substance_medication_contribution
      - medical_contribution
    knowledge_refs: [PSY_BELIEF_001, PSY_ASSESS_001]

  - id: PRE-SHORT-SLEEP
    before_action_objectives: [support_decreased_need_for_sleep, escalate_mania_from_sleep]
    require_unknowns_resolved_or_probed:
      - subjective_sleep_need
      - next_day_fatigue_or_energy
    knowledge_refs: [BIP_SLEEP_001, BIP_SLEEP_002]

  - id: PRE-DIAGNOSTIC-DEPTH
    before_action_objectives: [deepen_any_core6_diagnosis]
    require_unknowns_resolved_or_probed: []
    also_screen:
      - substance_medication_contribution
      - medical_contribution
    knowledge_refs: [BIP_ASSESS_001, PSY_ASSESS_001, DEP_ASSESS_001]

  - id: PRE-FUNCTION
    before_action_objectives: [confirm_clinical_significance]
    require_unknowns_resolved_or_probed:
      - functional_impairment
    knowledge_refs: [DEP_ASSESS_001, ANX_ASSESS_001, ADHD_DX_002]
```
