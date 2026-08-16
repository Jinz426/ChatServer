# Project Document & Implementation Status v0.3

## Purpose
This document is the canonical index for the repository's specifications, registries and executable prototypes. It prevents a documented idea from being mistaken for a completed data product.

## Status vocabulary
- **SPEC** — design/specification exists.
- **PROTOTYPE** — partial executable implementation exists.
- **INGESTION** — source adapters/data loading are required or underway.
- **VERIFY** — source, legal, licensing or factual verification remains.
- **PLANNED** — not implemented yet.
- **COMPLETE** — implementation + tests + source validation + provenance + licensing + versioning + monitoring are all present.

## Current repository layers

### Global knowledge / registries
| Area | Primary document | Current status |
|---|---|---|
| Master architecture | `GLOBAL_KNOWLEDGE_MASTER_PLAN_V0.2.md` | SPEC |
| Global completion audit | `GLOBAL_COMPLETION_AUDIT_V0.1.md` | AUDIT BASELINE |
| Country/exchange/currency | `GLOBAL_COUNTRY_EXCHANGE_CURRENCY_REGISTRY_V0.1.md` | SPEC / INGESTION |
| Banks | `GLOBAL_BANK_REGISTRY_V0.1.md` | SPEC / INGESTION |
| Exchanges/regulators/main boards | `GLOBAL_EXCHANGE_REGULATOR_MAINBOARD_REGISTRY_V0.1.md` | SPEC / INGESTION |
| Payment rails | `GLOBAL_PAYMENT_RAILS_REGISTRY_V0.1.md` | SPEC / INGESTION |
| Top 100,000 enterprises | `GLOBAL_TOP_100000_ENTERPRISE_REGISTRY_V0.1.md` | SPEC / INGESTION |
| Country regulatory instruments | `COUNTRY_LICENSE_REGISTRY_SCHEMA_V0.1.md` | SPEC / VERIFY |
| Global database ingestion model | `GLOBAL_DATABASE_UPDATE_V0.2.md` | SPEC / INGESTION |

### Science / technology
| Area | Primary document | Current status |
|---|---|---|
| AI observation | `AI_OBSERVATION_PROTOCOL.md` | SPEC |
| Biology / blood / genomics / proteins / species | `GLOBAL_BIOLOGICAL_KNOWLEDGE_REGISTRY_V0.1.md` | SPEC / INGESTION |
| CRISPR / biotechnology | `BIOTECH_CRISPR_AND_LIFE_SCIENCE_REGISTRY_V0.1.md` | SPEC / VERIFY |
| Electronics / brands / EMBED | `ELECTRONICS_BRAND_REGISTRY_AND_EMBEDDED_LANGUAGE_V0.1.md` | SPEC |

### AI / user-authorized ecosystem
| Area | Primary document | Current status |
|---|---|---|
| ChatGPT archive | `CHATGPT_ARCHIVE_PIPELINE.md` | SPEC / LOCAL INGESTION |
| Conversation thematic index | `CONVERSATION_ARCHIVE_INDEX.md` | CURATED INDEX |
| Siri / multi-model bridge | `SIRI_AND_MULTI_MODEL_BRIDGE.md` | SPEC |
| ORBIT router / work meter / ledger | `ORBIT_ROUTER_LEDGER_V0.1.md` | SPEC |
| Intel optimization | `ORBIT_INTEL_ACCELERATION.md` | SPEC |

### ORBIT runtime
| Component | Path | Current status |
|---|---|---|
| Language specification | `docs/ORBIT_LANGUAGE_SPEC_V0.1.md` | SPEC |
| Architecture | `docs/ORBIT_ARCHITECTURE_V0.2.md` | SPEC |
| Draft grammar | `docs/ORBIT_GRAMMAR_V0.1.md` | LEGACY DRAFT |
| Current grammar | `docs/ORBIT_GRAMMAR_V0.2.md` | SPEC / PROTOTYPE TARGET |
| Lexer | `orbit/lexer.py` | PROTOTYPE |
| Parser | `orbit/parser.py` | PROTOTYPE |
| AST | `orbit/ast.py` | PROTOTYPE |
| Semantic checker | `orbit/checker.py` | PROTOTYPE |
| Runtime README | `orbit/README.md` | DOCUMENTATION |

## Important consistency corrections

1. The original README previously showed the ORBIT lexer/parser/AST as unfinished even though prototypes now exist. It must mark them as prototype-level, not complete.
2. The older ORBIT grammar describes `world/location/product/evidence/flow`, while the current parser prototype implements `entity/observation`. Both concepts should not be presented as the same grammar. `ORBIT_GRAMMAR_V0.1.md` is therefore retained as a legacy draft and `ORBIT_GRAMMAR_V0.2.md` defines the current parser target.
3. The AST module and parser must use the same AST types.
4. Semantic checking must distinguish entity nodes from observation nodes instead of relying on the type of the first node in a program.
5. Global registries are specifications/ingestion plans unless actual records have been source-verified. No document should imply that all countries, banks, exchanges, companies or payment rails have already been populated.
6. Ranking targets such as "Top 100,000 enterprises" are coverage targets, not a claim that a single authoritative ranking contains 100,000 globally comparable companies.
7. International datasets (World Bank, IMF, BIS, WFE, etc.) are contextual/statistical sources and do not automatically replace national legal or regulatory registers.
8. Private user archives and sensitive biological/financial information must not be published merely because an importer can process them.

## Repository-wide data contract

Every world-data record should be able to carry:

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

## Evidence states

Use the same semantic distinction throughout the repository:

`OBSERVED → SOURCED → DERIVED → INFERRED → UNKNOWN`

A verified source does not automatically make every derived conclusion a verified fact. Transformations must retain lineage.

## Privacy / access classes

```text
PUBLIC
INSTITUTIONAL
CONTROLLED_ACCESS
RESTRICTED
PRIVATE
```

The public repository should contain public metadata, schemas, references and deliberately published material—not private account data, credentials, patient/donor records or confidential financial records.

## Completion gate

A component can only move to `COMPLETE` when all of these exist:

- executable implementation where applicable;
- automated tests;
- representative fixtures;
- source validation;
- entity-resolution checks;
- provenance/lineage;
- temporal/version handling;
- license/terms review;
- security/privacy review;
- monitoring/health checks;
- documentation and reproducible instructions.

## Immediate next priorities

1. Align parser → AST → checker.
2. Add ORBIT unit/type system.
3. Add evidence/provenance objects and ORBIT-IR.
4. Add canonical entity IDs and crosswalks.
5. Build source registry and adapter contract.
6. Build one fully verified country as an end-to-end reference implementation before scaling to 193 countries.
7. Add automated data-gap reporting.
8. Add CI tests and reproducible fixtures.
9. Add legal/licensing metadata checks.
10. Only then scale global ingestion toward the 100,000-enterprise and per-country targets.

## Principle

**Build one complete vertical slice before claiming global completeness.**
