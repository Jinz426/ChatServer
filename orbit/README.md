# ORBIT Runtime Prototype

This directory contains the first executable reference components for ORBIT v0.1.

## Current components
- `lexer.py` — tokenization
- `parser.py` — minimal entity/observation parser

## Example

```python
from orbit.parser import parse

program = '''
entity country "TH" {
  name "Thailand"
  iso2 "TH"
}
'''

print(parse(program))
```

## Next components
1. AST normalization
2. Type and unit checker
3. Entity resolver
4. Evidence/provenance checker
5. Permission checker
6. ORBIT-IR
7. Reference interpreter
8. Conformance tests

This is an experimental prototype and not yet a stable language implementation.
