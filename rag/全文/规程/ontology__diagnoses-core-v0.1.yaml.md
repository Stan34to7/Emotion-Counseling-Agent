# `ontology/diagnoses-core-v0.1.yaml`

```yaml
primary_system: ICD-11
compatibility_layer: DSM-5-TR mapping only
hypotheses_not_labels: true
core:
- id: depressive_episode
  domains:
  - DEP
- id: depressive_disorder
  domains:
  - DEP
- id: gad
  domains:
  - ANX
- id: panic_disorder
  domains:
  - ANX
- id: bipolar_disorder
  domains:
  - BIP
- id: manic_episode
  domains:
  - BIP
- id: hypomanic_episode
  domains:
  - BIP
- id: schizophrenia_spectrum_presentation
  domains:
  - PSY
- id: adhd
  domains:
  - ADHD
- id: self_harm_related_presentation
  domains:
  - SH
boundary_only_p1:
- ptsd
- ocd
- eating_disorder
- autism
- personality_disorder
- substance_use_disorder
```
