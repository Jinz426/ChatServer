# ORBIT Runtime Prototype

This directory contains the first executable reference components for ORBIT v0.1/v0.2 syntax.

## Current components
- `lexer.py` — deterministic tokenization
- `parser.py` — entity/observation parser producing normalized AST nodes
- `ast.py` — shared AST definitions
- `checker.py` — identifier uniqueness and observation-evidence checks
- `../tests/test_orbit.py` — initial parser/checker tests

## Example

```python
from orbit.parser import parse
from orbit.checker import check_program

program = parse('''
entity country "TH" {
  name "Thailand"
  iso2 "TH"
}
''')

check_program(program)
print(program)
```

## Current status

This is a **prototype**, not a stable compiler or runtime. The parser currently uses a small field-key set to disambiguate field names from identifier values. This will be replaced by a formal token-aware grammar.

## Next components
1. Complete type system
2. Unit and dimensional checker
3. Entity resolver
4. Evidence/provenance objects
5. Permission checker
6. ORBIT-IR
7. Reference interpreter
8. JSON/graph exporter
9. Conformance and property-based tests
10. Provider/runtime adapters

No global data source is implicitly trusted by the runtime. Source provenance and access policy remain external semantic inputs until the evidence layer is implemented.
