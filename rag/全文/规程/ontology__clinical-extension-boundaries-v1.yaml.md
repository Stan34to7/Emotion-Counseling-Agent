# `ontology/clinical-extension-boundaries-v1.yaml`

```yaml
version: "1.0.0"
status: ARCHITECTURE_READY_CONTENT_BLOCKED_EXTERNAL
shared_hypothesis_contract:
  required_fields:
    - supporting_evidence
    - counterevidence
    - confounds
    - missing_information
    - functional_impairment
    - temporal_requirement
    - alternative_explanations
  allowed_status: [insufficient, possible, supported, weakened, needs_assessment]
  forbid: [fake_probability, autonomous_diagnosis]
modules:
  depressive_spectrum: {runtime: CORE_IMPLEMENTED, expert_review: PENDING_EXTERNAL}
  anxiety_panic: {runtime: CORE_IMPLEMENTED, expert_review: PENDING_EXTERNAL}
  bipolar_spectrum: {runtime: CORE_IMPLEMENTED, expert_review: PENDING_EXTERNAL}
  adhd: {runtime: CORE_IMPLEMENTED, expert_review: PENDING_EXTERNAL}
  psychotic_symptoms: {runtime: CORE_IMPLEMENTED, expert_review: PENDING_EXTERNAL}
  self_harm_suicide: {runtime: SAFETY_SUPERVISOR_IMPLEMENTED, expert_review: PENDING_EXTERNAL}
  sleep_related: {runtime: BOUNDARY_IMPLEMENTED, expert_review: PENDING_EXTERNAL}
  adjustment_stress_reaction: {runtime: BOUNDARY_ONLY, expert_review: PENDING_EXTERNAL}
  ocd: {runtime: BOUNDARY_ONLY, expert_review: PENDING_EXTERNAL}
  ptsd_trauma_related: {runtime: BOUNDARY_ONLY, expert_review: PENDING_EXTERNAL}
  eating_disorders: {runtime: BOUNDARY_ONLY, expert_review: PENDING_EXTERNAL}
  substance_related: {runtime: CONFOUND_BOUNDARY_ONLY, expert_review: PENDING_EXTERNAL}
  autism_spectrum: {runtime: BOUNDARY_ONLY, expert_review: PENDING_EXTERNAL}
  personality_pathology: {runtime: BOUNDARY_ONLY_NO_DIAGNOSIS, expert_review: PENDING_EXTERNAL}
```
