"""ORBIT v0.1 semantic checks: identifiers, evidence and basic units."""
import re

ENTITY_ID_RE = re.compile(r"^[A-Za-z0-9_.:-]+$")

class OrbitCheckError(ValueError):
    pass

def check_program(nodes):
    seen = set()
    for node in nodes:
        ident = getattr(node, "entity_id", None) or getattr(node, "observation_id", None)
        if ident in seen:
            raise OrbitCheckError(f"Duplicate identifier: {ident}")
        if not ident or not ENTITY_ID_RE.match(ident):
            raise OrbitCheckError(f"Invalid identifier: {ident!r}")
        seen.add(ident)
        fields = getattr(node, "fields", {})
        if isinstance(node, type(nodes[0])) and "evidence" in fields:
            evidence = fields["evidence"]
            if evidence not in {"verified", "observed", "inferred", "unverified"}:
                raise OrbitCheckError(f"Unknown evidence status: {evidence}")
    return True
