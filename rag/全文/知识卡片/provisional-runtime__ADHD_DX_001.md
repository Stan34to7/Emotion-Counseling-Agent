# ADHD_DX_001 · ADHD full assessment required

来源文件：`knowledge-cards/provisional-runtime/ADHD_DX_001.yaml`

```yaml
id: ADHD_DX_001
type: DIAGNOSTIC_REQUIREMENT
title: ADHD full assessment required
clinical_claim: ADHD diagnosis requires specialist full clinical/psychosocial assessment, developmental
  and psychiatric history, observer reports/mental state — not rating scales alone.
applies_to:
- ADHD
phenomena:
- inattention
- hyperactivity
- impulsivity
supports: []
does_not_establish:
- adhd_from_rating_scale_alone
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
candidate_probes:
- QB-ADHD-DEV-01
- QB-ADHD-SETTING-01
next_if_positive: []
next_if_negative: []
sources:
- source_id: nice-ng87
  locator: 1.3.1; 1.3.2
  claim_id: CLM-ADHD-FULL-ASSESSMENT
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
  reason: NG87 1.3.1–1.3.2 direct
verification:
  source_verified: true
  structure_verified: true
  expert_reviewed: false
runtime_permission: PROVISIONAL_RUNTIME
```
