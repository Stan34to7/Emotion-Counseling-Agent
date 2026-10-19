# RDOC_LIM_001 · RDoC is not a diagnosis system

来源文件：`knowledge-cards/provisional-runtime/RDOC_LIM_001.yaml`

```yaml
id: RDOC_LIM_001
type: ASSESSMENT_LIMITATION
title: RDoC is not a diagnosis system
clinical_claim: RDoC is a research framework of functional domains/constructs spanning normal to abnormal;
  it is not a diagnostic classification system.
applies_to:
- cross_cutting
phenomena: []
supports: []
does_not_establish:
- any_icd_diagnosis_from_rdoc_construct
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
- source_id: nimh-rdoc-domains
  locator: Overview — six domains research framework
  claim_id: CLM-RDOC-NOT-DX
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
  gate_reason: semantic_source_audit_pass; expert review pending
  status: IMPLEMENTED_PENDING_EXPERT_REVIEW
audit:
  decision: KEEP
  reason: NIMH RDoC overview direct
verification:
  source_verified: true
  structure_verified: true
  expert_reviewed: false
runtime_permission: PROVISIONAL_RUNTIME
```
