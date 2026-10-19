# `formulation/formulation.schema.json`

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "CaseFormulation",
  "type": "object",
  "required": ["presenting_problems", "uncertainties", "evidence_refs"],
  "properties": {
    "presenting_problems": {"type": "array", "items": {"type": "string"}},
    "predisposing": {"type": "array", "items": {"$ref": "#/definitions/edge"}},
    "precipitating": {"type": "array", "items": {"$ref": "#/definitions/edge"}},
    "perpetuating": {"type": "array", "items": {"$ref": "#/definitions/edge"}},
    "protective": {"type": "array", "items": {"$ref": "#/definitions/edge"}},
    "clinical_hypotheses": {"type": "array", "items": {"type": "string"}},
    "uncertainties": {"type": "array", "items": {"type": "string"}},
    "evidence_refs": {"type": "array", "items": {"type": "string"}, "minItems": 1}
  },
  "definitions": {
    "edge": {
      "type": "object",
      "required": ["statement", "patient_evidence_refs"],
      "properties": {
        "statement": {"type": "string"},
        "patient_evidence_refs": {"type": "array", "items": {"type": "string"}, "minItems": 1},
        "confidence_band": {"type": "string", "enum": ["very_low", "low", "moderate", "high"]}
      }
    }
  }
}
```
