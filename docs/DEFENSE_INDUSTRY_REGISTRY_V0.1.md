# Global Defense Industry Registry v0.1

## Purpose
A public-source registry for classifying defense and military-services companies as part of the broader Global Enterprise Graph. The registry focuses on legal entities, ownership, industry classification, public financial/contract information, regulatory provenance and historical changes.

This is **not** a weapons-design, manufacturing-instruction, targeting, or export-control-evasion database.

## Classification hierarchy

### D01 — Aerospace & Aircraft
- military aircraft
- transport aircraft
- helicopters
- aerospace structures
- avionics

### D02 — Missiles, Rockets & Space Defense
- launch/space systems
- missile-sector companies
- propulsion businesses
- space-defense services

Records remain corporate/industrial metadata only.

### D03 — Naval & Maritime Defense
- naval shipbuilding
- submarines
- naval systems
- marine engineering
- ship repair and maintenance

### D04 — Land Systems
- armored-vehicle manufacturers
- military vehicle systems
- protected mobility
- land-system maintenance

### D05 — Defense Electronics
- radar
- sensors
- electronic systems
- communications equipment
- command-and-control systems
- navigation systems

### D06 — Cyber, Information & Intelligence Services
- cybersecurity
- information systems
- intelligence-support services
- secure communications

Classify publicly documented business activities; do not provide operational intrusion guidance.

### D07 — Engines, Propulsion & Power
- aircraft engines
- marine propulsion
- vehicle power systems
- turbines and associated industrial systems

### D08 — Munitions & Conventional Weapons Manufacturing
- publicly documented ammunition/munitions manufacturers
- conventional weapons companies

Only corporate and public regulatory/financial metadata is stored.

### D09 — Uncrewed / Autonomous Systems
- unmanned aircraft
- maritime autonomous systems
- ground robotic systems
- associated sensors and support services

No operational weaponization instructions are included.

### D10 — Defense Materials & Components
- armor materials
- specialty metals
- composites
- optics
- electronic components
- industrial components

### D11 — Maintenance, Repair & Overhaul (MRO)
- aircraft MRO
- naval maintenance
- vehicle maintenance
- depot services
- lifecycle support

### D12 — Logistics & Military Services
- logistics providers
- training services
- facilities management
- support services
- supply services

### D13 — Defense Software & Systems Integration
- systems integration
- simulation
- enterprise defense software
- mission-support software

### D14 — Research, Engineering & Testing
- defense R&D organizations
- engineering contractors
- testing/certification services
- laboratories where publicly documented

### D15 — Dual-use Industrial Groups
Companies with both civilian and defense business lines. Preserve separate business-segment classifications where available.

## Entity schema

```text
DefenseCompany
├── canonical_entity_id
├── legal_name
├── aliases
├── country
├── jurisdiction
├── parent_entity
├── subsidiaries
├── ownership_type
├── defense_sector_codes[]
├── civilian_sector_codes[]
├── official_website
├── regulator
├── license_or_authorization_reference
├── public_contract_references[]
├── defense_revenue
├── total_revenue
├── employees
├── listed_exchange
├── ticker
├── LEI
├── national_company_id
├── industrial_sites
├── historical_events[]
├── source_records[]
└── provenance
```

## Ownership categories
- STATE_OWNED
- STATE_CONTROLLED
- PUBLICLY_LISTED
- PRIVATELY_HELD
- SUBSIDIARY
- JOINT_VENTURE
- UNKNOWN

Ownership must be time-versioned because control can change.

## Geographic coverage
Use the Global Country Registry as the country backbone. A company may have:
- incorporation jurisdiction
- headquarters country
- operating countries
- manufacturing countries
- listing jurisdiction
- parent-company jurisdiction

These must not be conflated.

## Ranking sources
Potential public ranking/reference sources include:
- SIPRI Arms Industry Database / SIPRI Top 100
- national procurement and regulator sources
- company annual reports
- stock-exchange filings
- government contract notices
- corporate registries
- WIPO patent metadata where applicable

Ranking records must preserve:
`source + year + methodology + metric + retrieval_date`.

There is no single universal global ranking of every defense company. A ranking is a source-specific observation.

## Supply-chain integration
Defense companies can connect to the Global Enterprise Graph through:

```text
Defense Company
  -> Parent / Subsidiary
  -> Supplier
  -> Factory / Facility
  -> Product Category
  -> Material
  -> Element
  -> Bank
  -> Payment Rail
  -> Exchange
  -> Patent / IP
  -> Country
  -> Logistics
```

## Regulatory metadata
Where public, record:
- licensing authority
- procurement authority
- export-control authority
- sanctions status
- authorization status
- regulatory notices
- effective dates
- source URLs/identifiers

Do not infer legal status from an unrelated commercial database when an authoritative regulator record is available.

## Evidence model
Every important field should have provenance:

`OBSERVATION -> SOURCE -> RETRIEVAL_DATE -> VERSION -> EVIDENCE_STATUS`

Keep:
`OBSERVATION != CURATED_FACT != INFERENCE`

Conflicting sources should remain visible rather than silently merged.

## Safety boundary
This registry may organize public corporate, industrial, financial, ownership, procurement and regulatory information. It must not provide:
- weapon construction instructions
- manufacturing recipes or process optimization for weapons
- targeting assistance
- tactical operational guidance
- instructions to bypass export controls or sanctions
- unauthorized access to restricted defense information

## Implementation status
SPECIFICATION / REGISTRY DESIGN — v0.1

The existence of this schema does not mean that all companies or countries have already been ingested. Each record requires source verification and license review before being marked verified.
