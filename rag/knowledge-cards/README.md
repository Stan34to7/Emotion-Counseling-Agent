# Knowledge Cards

| Dir | Meaning |
|-----|---------|
| `provisional-runtime/` | Source+structure verified enough for agent use; **not** expert-final |
| `review/` | RESEARCH_ONLY / needs rewrite |
| `deprecated/` | Removed as clinical cards |
| `examples/` | Schema demos only |
| `promoted/` | Legacy path — empty redirect |

## Permission model

Separate:

1. `verification.source_verified`
2. `verification.structure_verified`
3. `verification.expert_reviewed`
4. `runtime_permission` ∈ `PROVISIONAL_RUNTIME` | `RESEARCH_ONLY` | `DEPRECATED` | `PRODUCTION_RUNTIME`

`SKILL_ALLOWED` is forbidden.
