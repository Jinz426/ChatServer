# ORBIT Grammar v0.2

This grammar is the current target for the executable `orbit/lexer.py` + `orbit/parser.py` prototype. The older `ORBIT_GRAMMAR_V0.1.md` remains as a historical draft for the earlier world/product syntax.

## Top-level grammar

```ebnf
program       = { declaration } ;
declaration   = entity | observation ;
entity        = "entity" identifier string block ;
observation   = "observation" string block ;
block         = "{" { field } "}" ;
field         = identifier value-sequence ;
value-sequence = value { value } ;
value         = string | number | identifier ;
identifier    = letter { letter | digit | "_" | "." | ":" | "-" } ;
number        = digit { digit } [ "." digit { digit } ] ;
string        = '"' { character } '"' ;
```

## Examples

```orbit
entity country "TH" {
  name "Thailand"
  iso2 "TH"
  iso3 "THA"
}

entity company "company:example" {
  legal_name "Example Corporation"
  jurisdiction "TH"
}

observation "obs:revenue:2026" {
  subject company "company:example"
  predicate revenue
  value 100000000 THB
  period 2026
  source "official-source"
  evidence verified
}
```

## Semantic rules

1. Entity identifiers are stable within a dataset namespace.
2. Observation identifiers must be unique within a program or import batch.
3. `value` may contain a number plus unit/currency identifiers, but semantic type checking happens after parsing.
4. Evidence status is not the same as truth; `verified` means the designated evidence rule passed, not that every inference derived from it is verified.
5. Source, observation time, publication time and effective time are separate concepts.
6. Permissions are checked by the runtime; capability declarations never grant permission automatically.

## Current implementation boundary

The v0.2 parser intentionally handles a small subset. It does not yet implement the complete semantic grammar, query language, imports, modules, expressions, relations or ORBIT-IR.

The next parser milestone should replace bounded value collection with a token-aware field grammar and then add explicit AST nodes for quantities, entity references, dates and provenance.

## Compatibility policy

Syntax additions require:
- a version bump or explicitly backward-compatible change;
- lexer/parser tests;
- AST representation;
- semantic validation rules;
- example programs;
- documentation update.
