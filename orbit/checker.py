"""ORBIT v0.1 semantic checks: identifiers and evidence status."""
import re
from .ast import EntityNode, ObservationNode, Program

ENTITY_ID_RE = re.compile(r"^[A-Za-z0-9_.:-]+$")
EVIDENCE_STATUSES = {"verified", "observed", "inferred", "unverified"}

class OrbitCheckError(ValueError):
    pass

def check_program(program):
    if isinstance(program, Program):
        nodes = program.nodes
    else:
        nodes = list(program)

    seen = set()
    for node in nodes:
        if isinstance(node, EntityNode):
            ident = node.entity_id
        elif isinstance(node, ObservationNode):
            ident = node.observation_id
        else:
            raise OrbitCheckError(f"Unsupported AST node: {type(node).__name__}")

        if ident in seen:
            raise OrbitCheckError(f"Duplicate identifier: {ident}")
        if not ident or not ENTITY_ID_RE.match(ident):
            raise OrbitCheckError(f"Invalid identifier: {ident!r}")
        seen.add(ident)

        fields = node.fields
        if isinstance(node, ObservationNode) and "evidence" in fields:
            evidence = fields["evidence"]
            if evidence not in EVIDENCE_STATUSES:
                raise OrbitCheckError(f"Unknown evidence status: {evidence}")

    return True
