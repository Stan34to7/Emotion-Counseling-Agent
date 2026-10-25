# `personality/functional-personality.yaml`

```yaml
version: "0.1.0"
constructs:
  - {id: self_esteem, requires: [definition, evidence_rule, insufficient_for]}
  - {id: self_efficacy, requires: [definition, evidence_rule, insufficient_for]}
  - {id: agency, requires: [definition, evidence_rule, insufficient_for]}
  - {id: autonomy, requires: [definition, evidence_rule, insufficient_for]}
  - {id: need_for_control, requires: [definition, evidence_rule, insufficient_for]}
  - {id: reward_sensitivity, requires: [definition, evidence_rule, insufficient_for]}
  - {id: threat_sensitivity, requires: [definition, evidence_rule, insufficient_for]}
  - {id: achievement_motivation, requires: [definition, evidence_rule, insufficient_for]}
  - {id: status_motivation, requires: [definition, evidence_rule, insufficient_for]}
  - {id: affiliation_motivation, requires: [definition, evidence_rule, insufficient_for]}
  - {id: trust, requires: [definition, evidence_rule, insufficient_for]}
  - {id: intimacy, requires: [definition, evidence_rule, insufficient_for]}
  - {id: dependency, requires: [definition, evidence_rule, insufficient_for]}
  - {id: rejection_sensitivity, requires: [definition, evidence_rule, insufficient_for]}
  - {id: conflict_style, requires: [definition, evidence_rule, insufficient_for]}
  - {id: boundary_style, requires: [definition, evidence_rule, insufficient_for]}
  - {id: emotion_regulation, requires: [definition, evidence_rule, insufficient_for]}
  - {id: cognitive_flexibility, requires: [definition, evidence_rule, insufficient_for]}
  - {id: rumination, requires: [definition, evidence_rule, insufficient_for]}
  - {id: perfectionism, requires: [definition, evidence_rule, insufficient_for]}
  - {id: need_for_certainty, requires: [definition, evidence_rule, insufficient_for]}
  - {id: impulsivity, requires: [definition, evidence_rule, insufficient_for]}
  - {id: risk_tolerance, requires: [definition, evidence_rule, insufficient_for]}
  - {id: identity_coherence, requires: [definition, evidence_rule, insufficient_for]}
  - {id: value_stability, requires: [definition, evidence_rule, insufficient_for]}
note: "Full operational definitions beyond schema are B/C tier; v0.1 freezes namespace + inference policy."
```
