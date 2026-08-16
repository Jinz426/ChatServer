"""ORBIT v0.1 reference lexer: intentionally small, deterministic prototype."""
from dataclasses import dataclass
import re

TOKEN_RE = re.compile(r'''(?P<WS>\s+)|(?P<COMMENT>#[^\n]*)|(?P<STRING>"(?:\\.|[^"\\])*")|(?P<NUMBER>\d+(?:\.\d+)?)|(?P<ID>[A-Za-z_][A-Za-z0-9_.:-]*)|(?P<SYMBOL>[{}()=,])''')

@dataclass(frozen=True)
class Token:
    kind: str
    value: str
    position: int

def lex(source: str):
    pos = 0
    while pos < len(source):
        m = TOKEN_RE.match(source, pos)
        if not m:
            raise SyntaxError(f"Unexpected character at {pos}: {source[pos]!r}")
        kind, value = m.lastgroup, m.group()
        pos = m.end()
        if kind not in {"WS", "COMMENT"}:
            yield Token(kind, value, m.start())
    yield Token("EOF", "", len(source))
