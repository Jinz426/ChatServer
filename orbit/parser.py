"""ORBIT v0.1 reference parser prototype."""
from dataclasses import dataclass
from .lexer import lex, Token

@dataclass
class Entity:
    type: str
    id: str
    fields: dict

@dataclass
class Observation:
    id: str
    fields: dict

class Parser:
    def __init__(self, source: str):
        self.tokens = list(lex(source))
        self.i = 0

    def peek(self):
        return self.tokens[self.i]

    def pop(self):
        t = self.tokens[self.i]; self.i += 1; return t

    def expect(self, kind, value=None):
        t = self.pop()
        if t.kind != kind or (value is not None and t.value != value):
            raise SyntaxError(f"Expected {kind} {value or ''} at {t.position}")
        return t

    def value(self):
        t = self.pop()
        if t.kind in {"STRING", "ID", "NUMBER"}:
            return t.value.strip('"')
        raise SyntaxError(f"Expected value at {t.position}")

    def block(self):
        self.expect("SYMBOL", "{")
        fields = {}
        while not (self.peek().kind == "SYMBOL" and self.peek().value == "}"):
            key = self.expect("ID").value
            vals = []
            while not (self.peek().kind == "ID" and self.tokens[self.i + 1].value == "{") and not (self.peek().kind == "SYMBOL" and self.peek().value == "}"):
                vals.append(self.value())
                if self.peek().kind == "EOF": break
            fields[key] = vals[0] if len(vals) == 1 else vals
        self.expect("SYMBOL", "}")
        return fields

    def parse(self):
        nodes = []
        while self.peek().kind != "EOF":
            kind = self.expect("ID").value
            ident_type = self.expect("ID").value
            ident = self.value()
            fields = self.block()
            if kind == "entity": nodes.append(Entity(ident_type, ident, fields))
            elif kind == "observation": nodes.append(Observation(ident, fields))
            else: raise SyntaxError(f"Unsupported top-level form: {kind}")
        return nodes

def parse(source: str):
    return Parser(source).parse()
