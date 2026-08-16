# ORBIT × Global World Knowledge

> A user-authorized, evidence-based framework for connecting AI, software, physical-world knowledge, resources, products, supply chains, and historical context.

## 🧭 What is this?

This repository is the evolving home of two connected projects:

1. **ORBIT Language** — a provider-neutral language and semantic layer for describing computation, data, locations, objects, relationships, evidence and AI tasks.
2. **Global World Knowledge** — a structured world-observation system connecting coordinates, buildings, roads, products, prices, resources, production, transport, recycling and history.

The project is designed to let humans and authorized AI systems observe the same world through a common, versioned vocabulary while preserving evidence and uncertainty.

## 🧠 User Knowledge Layer

ORBIT can maintain a **User Knowledge Graph** from information that the user explicitly authorizes or imports.

```text
Authorized Sources
      ↓
Permission / Consent Layer
      ↓
Import / Connector
      ↓
Privacy & Redaction
      ↓
User Knowledge Graph
      ↓
ORBIT Semantic Layer
      ↓
AI Models / Tools
```

Possible sources include:

- ChatGPT data exports
- GitHub repositories
- local documents
- project files
- notes
- calendars
- photos and media metadata
- other AI conversation exports
- explicitly connected services

### 🔐 Data boundary

**No component should silently read a user's entire device, account, private messages or cloud storage.** Data must be supplied through an explicit export, connector, permission or import process.

The system should record the state of every source as:

`NOT_CONNECTED → REQUESTED → AUTHORIZED → IMPORTED → INDEXED → REVOKED`

Revocation must prevent future ingestion and should support deletion of derived indexes where applicable.

## 📚 Knowledge categories

The project now includes registry specifications for:

- UN / ISO / WIPO / IANA / ICANN / ITU / IEEE source layers
- countries, jurisdictions and official-source registries
- banks and banking regulators
- currencies and exchange infrastructure
- exchanges, regulators, main boards and securities identifiers
- global payment rails
- enterprises and corporate hierarchies, including the Top-100,000 coverage target
- elements, materials and manufacturing
- electronics brands and the EMBED device language
- genomics, proteins, species, biodiversity and biobanks
- CRISPR and adjacent life-science fields
- products, prices and supply chains
- GIS / physical-world observations
- evidence, provenance and historical change

See [`docs/PROJECT_DOCUMENT_STATUS_V0.3.md`](docs/PROJECT_DOCUMENT_STATUS_V0.3.md) for the canonical document/status index.

Sensitive information should be minimized and never committed to a public repository without an explicit decision to publish it.

## 🌍 Global World Knowledge

The world model connects:

`coordinate → space → building → people → roads → commerce → product → price → production → supply chain → resources → lifecycle → recycling → history`

See [`GLOBAL_WORLD_KNOWLEDGE.md`](GLOBAL_WORLD_KNOWLEDGE.md) and [`docs/GLOBAL_KNOWLEDGE_MASTER_PLAN_V0.2.md`](docs/GLOBAL_KNOWLEDGE_MASTER_PLAN_V0.2.md).

## 🪐 ORBIT Language

ORBIT aims to unify concepts rather than merge unrelated source code or tokenizers. Provider-specific languages remain native behind adapters.

```text
Swift / C / C++ / Rust / Python / JavaScript / SQL / ML systems / GIS
                         ↓
                  ORBIT semantic layer
                         ↓
             AST → ORBIT-IR → backends
```

The executable prototype is under `orbit/`:

- `orbit/lexer.py` — lexer prototype
- `orbit/parser.py` — parser prototype
- `orbit/ast.py` — normalized AST
- `orbit/checker.py` — identifier/evidence checks

The current parser grammar is [`docs/ORBIT_GRAMMAR_V0.2.md`](docs/ORBIT_GRAMMAR_V0.2.md). The older v0.1 grammar is retained as a historical draft.

See [`docs/ORBIT_LANGUAGE_SPEC_V0.1.md`](docs/ORBIT_LANGUAGE_SPEC_V0.1.md) and [`docs/ORBIT_ARCHITECTURE_V0.2.md`](docs/ORBIT_ARCHITECTURE_V0.2.md).

## 🤖 Multi-model AI

AI providers connect through adapters rather than receiving unrestricted access to each other or to user data.

```text
Siri / Apple Intelligence / Local AI / Cloud AI
                     ↓
                ORBIT Bridge
                     ↓
              Semantic Message
                     ↓
             Router + Evidence
                     ↓
             Global Knowledge
```

See [`docs/SIRI_AND_MULTI_MODEL_BRIDGE.md`](docs/SIRI_AND_MULTI_MODEL_BRIDGE.md).

## 💰 AI work and value ledger

The project distinguishes provider billing tokens from the cross-provider **OSU (ORBIT Semantic Unit)** workload measure.

```text
User task → quote → authorization → AI work → usage → cost → ledger → settlement
```

No token is treated as money merely because software assigns it a name. Monetary settlement requires appropriate authorization, contracts, payment infrastructure and applicable laws.

See [`docs/ORBIT_ROUTER_LEDGER_V0.1.md`](docs/ORBIT_ROUTER_LEDGER_V0.1.md).

## 💻 Hardware adaptation

ORBIT is intended to optimize for the hardware actually available rather than pretending software can turn one physical chip into another.

The first hardware research target is Intel x86-64, with future Apple Silicon and other backends.

See [`docs/ORBIT_INTEL_ACCELERATION.md`](docs/ORBIT_INTEL_ACCELERATION.md).

## 📜 Conversation archive

The repository contains a recovered thematic index of long-running ChatGPT discussions. It is **not a complete account export**.

See [`docs/CONVERSATION_ARCHIVE_INDEX.md`](docs/CONVERSATION_ARCHIVE_INDEX.md) and [`docs/CHATGPT_ARCHIVE_PIPELINE.md`](docs/CHATGPT_ARCHIVE_PIPELINE.md).

A true historical archive requires the user's own ChatGPT data export or conversation files.

## 🔬 Evidence standard

Every important claim should distinguish:

- **Observed**
- **Sourced**
- **Derived**
- **Inferred**
- **Unknown**

Forensic-inspired reasoning follows:

`observation → evidence → hypothesis → corroboration → alternatives → conclusion → revision`

AI agreement is not proof. Correlation is not automatically causation.

## 🗂️ Repository map

```text
.
├── README.md
├── GLOBAL_WORLD_KNOWLEDGE.md
├── examples/
├── schemas/
├── docs/
│   ├── PROJECT_DOCUMENT_STATUS_V0.3.md
│   ├── GLOBAL_KNOWLEDGE_MASTER_PLAN_V0.2.md
│   ├── GLOBAL_COMPLETION_AUDIT_V0.1.md
│   ├── GLOBAL_DATABASE_UPDATE_V0.2.md
│   ├── GLOBAL_COUNTRY_EXCHANGE_CURRENCY_REGISTRY_V0.1.md
│   ├── GLOBAL_BANK_REGISTRY_V0.1.md
│   ├── GLOBAL_EXCHANGE_REGULATOR_MAINBOARD_REGISTRY_V0.1.md
│   ├── GLOBAL_PAYMENT_RAILS_REGISTRY_V0.1.md
│   ├── GLOBAL_TOP_100000_ENTERPRISE_REGISTRY_V0.1.md
│   ├── COUNTRY_LICENSE_REGISTRY_SCHEMA_V0.1.md
│   ├── GLOBAL_BIOLOGICAL_KNOWLEDGE_REGISTRY_V0.1.md
│   ├── BIOTECH_CRISPR_AND_LIFE_SCIENCE_REGISTRY_V0.1.md
│   ├── ELECTRONICS_BRAND_REGISTRY_AND_EMBEDDED_LANGUAGE_V0.1.md
│   ├── AI_OBSERVATION_PROTOCOL.md
│   ├── ORBIT_LANGUAGE_SPEC_V0.1.md
│   ├── ORBIT_ARCHITECTURE_V0.2.md
│   ├── ORBIT_GRAMMAR_V0.1.md
│   ├── ORBIT_GRAMMAR_V0.2.md
│   ├── ORBIT_INTEL_ACCELERATION.md
│   ├── SIRI_AND_MULTI_MODEL_BRIDGE.md
│   ├── ORBIT_ROUTER_LEDGER_V0.1.md
│   ├── CONVERSATION_ARCHIVE_INDEX.md
│   └── CHATGPT_ARCHIVE_PIPELINE.md
├── orbit/
│   ├── lexer.py
│   ├── parser.py
│   ├── ast.py
│   ├── checker.py
│   └── README.md
└── tools/
    └── import_chatgpt_export.py
```

## 🚀 Roadmap

### Phase 1 — Foundation
- [x] World Knowledge specification
- [x] Observation schema
- [x] Product/price schema
- [x] AI observation protocol
- [x] ORBIT language specification
- [x] Intel optimization strategy
- [x] Multi-model bridge concept
- [x] Token/value ledger concept
- [x] User Knowledge permission model
- [x] Global registry architecture

### Phase 2 — Runtime prototype
- [x] ORBIT lexer prototype
- [x] ORBIT parser prototype
- [x] Normalized AST prototype
- [x] Basic identifier/evidence checker prototype
- [ ] type and unit checker
- [ ] entity resolver
- [ ] full evidence/provenance checker
- [ ] permission engine
- [ ] ORBIT-IR
- [ ] provider adapters
- [ ] hardware capability probe
- [ ] token/work meter implementation
- [ ] ledger implementation
- [ ] conformance test suite

### Phase 3 — World intelligence
- [ ] image observation pipeline
- [ ] GIS layer
- [ ] product recognition
- [ ] price normalization
- [ ] supply-chain graph
- [ ] historical timeline
- [ ] knowledge graph
- [ ] data-gap engine
- [ ] conflict-resolution engine

### Phase 4 — Global ingestion
- [ ] UN/ISO country master
- [ ] official-source registry for all jurisdictions
- [ ] central-bank / banking-regulator adapters
- [ ] exchange/regulator/main-board adapters
- [ ] payment-rail adapters
- [ ] enterprise ranking/source adapters
- [ ] materials/electronics sources
- [ ] biological/scientific sources
- [ ] per-country coverage reports

### Phase 5 — User-authorized AI ecosystem
- [ ] ChatGPT export ingestion
- [ ] additional AI export adapters
- [ ] Apple/Siri App Intents prototype
- [ ] local knowledge index
- [ ] consent dashboard
- [ ] revocation and deletion workflow

### Phase 6 — Public platform
- [ ] dashboards
- [ ] machine-readable APIs
- [ ] source/provenance viewer
- [ ] global data-gap map
- [ ] security/legal audit
- [ ] reproducible releases

## ⚖️ Principles

1. User control before automation.
2. Evidence before certainty.
3. Open standards before vendor lock-in.
4. Interoperability without unrestricted access.
5. Privacy by design.
6. Version everything that changes.
7. Separate observation from inference.
8. Separate workload accounting from money.
9. Build experimentally and measure real performance.
10. Make the system useful to people before making it powerful.
11. **Never claim global completeness until the underlying records are actually verified.**

## License

Project licensing and third-party component notices must be defined before redistributing third-party source code. See each upstream project's license and NOTICE requirements.
