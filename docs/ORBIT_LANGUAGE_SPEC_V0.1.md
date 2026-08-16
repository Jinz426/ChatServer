# ORBIT Language Specification v0.1

## Overview
ORBIT is a proposed vendor-neutral language for describing, connecting, validating and reasoning over world entities, observations, evidence, devices, organizations, markets and scientific knowledge.

ORBIT is not intended to replace existing programming languages. It is a declarative knowledge/interoperability language that can compile into an intermediate representation (ORBIT-IR) and interoperate with conventional runtimes.

## Design goals
- Human-readable
- Machine-readable
- Strong types and units
- Canonical entity identifiers
- Explicit provenance
- Temporal versioning
- Evidence before inference
- Permission-aware capabilities
- Vendor-neutral interoperability
- Deterministic serialization
- Extensible schemas
- Safe failure

## Core concepts

```orbit
entity country "TH" {
  name "Thailand"
  iso2 "TH"
  iso3 "THA"
}

entity company "example" {
  name "Example Corporation"
  jurisdiction "TH"
}

observation "obs-001" {
  subject company "example"
  predicate revenue
  value 100000000 THB
  period 2026
  source "official-source"
  evidence verified
}
```

## Type system
Primitive types:
- string
- integer
- decimal
- boolean
- date
- datetime
- duration
- identifier
- entity-reference

Domain types:
- currency
- unit
- geographic-coordinate
- quantity
- percentage
- financial-value
- physical-measurement
- scientific-measurement

Units must be explicit where applicable. Currency conversion is a separate operation and must preserve the source currency, rate source, rate date and method.

## Entity model
Every entity should have:
- canonical ID
- entity type
- jurisdiction where applicable
- aliases
- parent/child relations
- validity interval
- source references
- status

Example:

```orbit
entity bank "bank:TH:example" {
  legal_name "Example Bank Public Company Limited"
  jurisdiction "TH"
  license_status active
  parent entity "company:example-group"
}
```

## Provenance
ORBIT distinguishes:

`OBSERVATION != CURATED_FACT != INFERENCE`

Example:

```orbit
observation "price-001" {
  subject product "product:123"
  predicate retail_price
  value 59.90 THB
  observed_at 2026-08-17T10:00:00+07:00
  source "source:official-store"
  evidence verified
}
```

## Temporal model
Facts can have validity intervals and observation timestamps:

```orbit
fact "license-001" {
  subject bank "bank:TH:example"
  predicate license_status
  value active
  valid_from 2025-01-01
  observed_at 2026-08-17T00:00:00Z
}
```

## Relations
Supported relation categories include:
- owns
- subsidiary_of
- operates
- manufactures
- supplies
- located_in
- listed_on
- regulated_by
- licensed_by
- uses_material
- contains_element
- implements_standard
- supports_protocol
- cites
- derived_from

## Capability and permission bridge
ORBIT can consume EMBED device profiles:

```orbit
use device "device:example" {
  require capability compute
  require permission read.system_info
}
```

Capabilities do not automatically grant permissions.

## Query concept
A future ORBIT query syntax may support entity, relationship, time and evidence constraints:

```orbit
query companies {
  where jurisdiction == "TH"
  where evidence == verified
  order_by revenue desc
  limit 100
}
```

## Modules
Proposed standard modules:

```text
orbit.core
orbit.entity
orbit.geo
orbit.time
orbit.units
orbit.currency
orbit.finance
orbit.payment
orbit.market
orbit.company
orbit.product
orbit.material
orbit.internet
orbit.science
orbit.biology
orbit.device
orbit.evidence
orbit.permission
orbit.ai
orbit.governance
```

## ORBIT-IR
The compiler should lower source code into a stable intermediate representation:

```text
ORBIT source
   -> lexer
   -> parser
   -> AST
   -> type/unit checker
   -> provenance checker
   -> permission checker
   -> ORBIT-IR
   -> runtime/provider adapters
```

## Safety and trust
ORBIT should refuse to silently promote unverified data to verified facts. Sensitive datasets require access controls and should be represented by references/metadata when direct access is unauthorized.

The language must not provide unrestricted privilege escalation, unauthorized device control, unauthorized access to private data, or unsafe biological operational guidance.

## Implementation roadmap
1. Grammar and tokenizer
2. Lexer
3. Parser
4. AST
5. Type and unit checker
6. Entity resolver
7. Evidence/provenance checker
8. Permission checker
9. ORBIT-IR
10. Reference interpreter
11. Provider adapters
12. Test suite and conformance tests

## Status
Specification prototype. Syntax is intentionally versioned and may change before a stable 1.0 release.
