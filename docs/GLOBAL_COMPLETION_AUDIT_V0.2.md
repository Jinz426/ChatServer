# Global Completion Audit v0.2

## Audit date
2026-08-17

## Purpose
Reconcile the repository's documented architecture with the executable code currently present. This audit supersedes the status assumptions in v0.1 where they conflict with the current repository.

## Status legend
- SPEC — specification/design exists.
- PROTOTYPE — partial executable implementation exists.
- INGESTION — source adapters or data population remain.
- VERIFY — source/legal/licensing verification remains.
- PLANNED — not implemented.
- COMPLETE — implementation, tests, provenance, validation, licensing and operational controls are all present.

## Key findings

### ORBIT runtime
- Lexer: **PROTOTYPE** (`orbit/lexer.py`).
- Parser: **PROTOTYPE** (`orbit/parser.py`).
- Normalized AST: **PROTOTYPE** (`orbit/ast.py`).
- Basic identifier/evidence checker: **PROTOTYPE** (`orbit/checker.py`).
- Type/unit system: **PLANNED**.
- Entity resolution: **PLANNED**.
- Full evidence/provenance checker: **PLANNED**.
- Permission engine: **PLANNED**.
- ORBIT-IR: **PLANNED**.
- Runtime/provider adapters: **PLANNED**.
- Conformance tests: **PLANNED**.

### Documentation consistency
- Current parser grammar is `docs/ORBIT_GRAMMAR_V0.2.md`.
- `docs/ORBIT_GRAMMAR_V0.1.md` is retained as a legacy draft and must not be described as the current parser grammar.
- `docs/PROJECT_DOCUMENT_STATUS_V0.3.md` is the canonical document/status index.
- README roadmap has been synchronized with current prototype status.

### Global registries
The repository contains specifications for countries, banks, exchanges, currencies, payment rails, enterprises, regulatory instruments, electronics, biology and CRISPR. These are **not** equivalent to having every global record ingested and verified.

The following remain primarily **SPEC / INGESTION / VERIFY**:
- 193-country source registry
- country bank registers
- exchange/regulator/main-board registry
- global payment-rail registry
- top-100,000 enterprise coverage
- materials/electronics registry
- biological/scientific registry
- country license/regulatory registry

## Canonical data contract

All scalable ingestion should converge on:

```text
canonical_entity_id
entity_type
jurisdiction
source_id
source_url
source_authority
source_version
methodology_version
observed_at
published_at
retrieved_at
effective_from
effective_until
value
unit
currency
status
evidence_type
confidence
license_status
access_class
provenance
```

## Evidence contract

The repository uses:

`OBSERVED → SOURCED → DERIVED → INFERRED → UNKNOWN`

These states must not be collapsed. A model's confidence is not a substitute for source evidence.

## Registry completion rule

A registry is **not complete** merely because its schema or README exists. A record is considered verified only when its source, identity, time/version, provenance and applicable access/license conditions are recorded.

## Global coverage targets

- UN Member States: 193-country backbone.
- Global enterprises: coverage target up to 100,000 significant entities using multiple ranking/source families.
- Per-country enterprises: target up to 10,000 per country where public data permits; this is a coverage target, not a claim that every country has 10,000 eligible enterprises or that all records are currently ingested.
- Payment rails: global system-level registry, not payment-account access.
- Banks: official institution/license registry where public.
- Biological data: public scientific metadata and authorized datasets; no private donor/patient records.

## Priority blockers before claiming global completeness

1. Canonical ID and ontology implementation.
2. Source registry and adapter framework.
3. Entity resolution/deduplication.
4. Temporal/version model.
5. Unit/currency/time normalization.
6. Provenance/data-lineage graph.
7. Automated data-quality and conflict detection.
8. One end-to-end fully verified country implementation.
9. Representative ingestion tests.
10. License/terms enforcement.
11. Security/privacy controls.
12. Monitoring and reproducible releases.

## Next audit gate

The next milestone should be a **single-country vertical slice** that goes from official country source → regulator → bank → payment rail → currency → exchange → enterprise → product/material observation → provenance → ORBIT query, with automated tests and a documented data-gap report.

Only after that slice is reproducible should ingestion scale outward to all 193 countries and the large enterprise targets.
