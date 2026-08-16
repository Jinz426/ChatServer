"""ORBIT v0.1 reference parser prototype."""
from .lexer import lex
from .ast import EntityNode, ObservationNode, Program

# Temporary keyword set for the v0.2 prototype. A full grammar will replace
# this heuristic with explicit field/value productions.
FIELD_KEYS = {
    "name", "iso2", "iso3", "iso_numeric", "legal_name", "jurisdiction",
    "license_status", "parent", "subject", "predicate", "value", "period",
    "source", "evidence", "observed_at", "published_at", "valid_from",
    "valid_until", "status", "confidence"
}

class Parser:
    def __init__(self, source: str):
        self.tokens = list(lex(source))
        self.i = 0

    def peek(self, offset=0):
        index = min(self.i + offset, len(self.tokens) - 1)
        return self.tokens[index]

    def pop(self):
        token = self.peek()
        self.i += 1
        return token

    def expect(self, kind, value=None):
        token = self.pop()
        if token.kind != kind or (value is not None and token.value != value):
            expected = f"{kind} {value}" if value is not None else kind
            raise SyntaxError(f"Expected {expected} at {token.position}; got {token.kind} {token.value!r}")
        return token

    def value(self):
        token = self.pop()
        if token.kind in {"STRING", "ID", "NUMBER"}:
            return token.value.strip('"')
        raise SyntaxError(f"Expected value at {token.position}")

    def block(self):
        self.expect("SYMBOL", "{")
        fields = {}
        while not (self.peek().kind == "SYMBOL" and self.peek().value == "}"):
            if self.peek().kind == "EOF":
                raise SyntaxError("Unterminated block")
            key = self.expect("ID").value
            values = []
            while len(values) < 4:
                token = self.peek()
                if token.kind in {"STRING", "NUMBER"}:
                    values.append(self.value())
                    continue
                if token.kind == "ID":
                    if token.value in FIELD_KEYS:
                        break
                    values.append(self.value())
                    continue
                break
            if not values:
                raise SyntaxError(f"Field {key!r} requires a value at {self.peek().position}")
            fields[key] = values[0] if len(values) == 1 else values
        self.expect("SYMBOL", "}")
        return fields

    def parse(self):
        nodes = []
        while self.peek().kind != "EOF":
            declaration = self.expect("ID").value
            entity_type = self.expect("ID").value
            identifier = self.value()
            fields = self.block()
            if declaration == "entity":
                nodes.append(EntityNode(entity_type, identifier, fields))
            elif declaration == "observation":
                nodes.append(ObservationNode(identifier, fields))
            else:
                raise SyntaxError(f"Unsupported top-level declaration: {declaration}")
        return Program(nodes)

def parse(source: str):
    return Parser(source).parse()
