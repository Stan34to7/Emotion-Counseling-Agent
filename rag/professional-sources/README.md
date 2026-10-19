# Professional Sources

Drop authoritative artifacts here. **Do not** commit copyrighted full manuals if legal counsel forbids it; registry URLs + local private drops are enough for extraction workstations.

## Buckets

| Bucket | Expected content |
|--------|------------------|
| `icd11/` | ICD-11 CDDR PDF or excerpt notes + page map |
| `mhgap/` | mhGAP-IG 2.0 / guideline PDFs |
| `nice/` | Pinned NICE guideline PDFs or HTML exports |
| `apa/` | Structure notes only unless licensed |
| `rdoc/` | RDoC domain matrix exports / notes |
| `psychometrics/` | IPIP item lists, license notes for other scales |
| `papers/` | Selected reviews; expert elicitation writeups |
| `licensed_tools/` | Placeholder + license proof only — never leak instrument text to public git |

## Workflow

1. Add/confirm entry in `source-registry.yaml`
2. Place file or `SOURCE.md` pointer in the bucket
3. Set `status: dropped` / `status: notes_only` in registry
4. Extract → `knowledge-cards/draft/`
