"""ORBIT v0.1 normalized AST nodes."""
from dataclasses import dataclass, field
from typing import Any

@dataclass
class EntityNode:
    entity_type: str
    entity_id: str
    fields: dict[str, Any] = field(default_factory=dict)

@dataclass
class ObservationNode:
    observation_id: str
    fields: dict[str, Any] = field(default_factory=dict)

@dataclass
class Program:
    nodes: list[Any] = field(default_factory=list)
