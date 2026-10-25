# `personality/personality.schema.json`

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "PersonalityConstructState",
  "type": "object",
  "required": ["construct", "layer", "value_band", "confidence_band", "stability_band", "supporting_evidence", "counter_evidence"],
  "properties": {
    "construct": {"type": "string"},
    "layer": {"type": "string", "enum": ["STATE", "EPISODE", "PATTERN", "TRAIT", "STRUCTURAL_PERSONALITY"]},
    "value_band": {"type": "string", "enum": ["low", "moderate", "high", "unknown"]},
    "confidence_band": {"type": "string", "enum": ["very_low", "low", "moderate", "high"]},
    "stability_band": {"type": "string", "enum": ["unknown", "low", "moderate", "high"]},
    "supporting_evidence": {"type": "array", "items": {"type": "string"}},
    "counter_evidence": {"type": "array", "items": {"type": "string"}},
    "contexts": {"type": "array", "items": {"type": "string"}},
    "exceptions": {"type": "array", "items": {"type": "string"}},
    "alternative_explanations": {"type": "array", "items": {"type": "string"}},
    "source_mode": {"type": "string", "enum": ["conversation_inference", "formal_psychometric_score"]}
  }
}
```
