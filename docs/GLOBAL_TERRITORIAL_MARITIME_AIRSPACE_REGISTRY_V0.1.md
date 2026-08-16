# Global Territorial, Maritime & Airspace Registry v0.1

## Purpose
A provenance-first registry for representing land territories, maritime zones, airspace, jurisdictions, administration, sovereignty claims and boundary evidence.

This registry deliberately separates sovereignty, administration, jurisdiction, claims and operational responsibility. A disputed or unresolved area must not be forced into a single ownership field.

## Core model

```text
Geographic Area
├── Land Territory
├── Internal Waters
├── Archipelagic Waters
├── Territorial Sea
├── Contiguous Zone
├── Exclusive Economic Zone (EEZ)
├── Continental Shelf
├── High Seas
└── Airspace / Flight Information Region (FIR)
```

## Legal concepts

### Land
Store:
- sovereign state / claimant(s)
- administering authority
- legal status
- treaty or legal instrument
- boundary geometry
- effective dates
- dispute status

### Maritime zones
Store separately:
- baseline
- internal waters
- territorial sea
- contiguous zone
- EEZ
- continental shelf
- high seas
- maritime delimitation agreements
- deposited coordinates/charts

Under UNCLOS, territorial-sea sovereignty extends to the adjacent belt of sea and to the airspace over it; the territorial sea may extend up to 12 nautical miles from the applicable baselines. citeturn0search2

The EEZ is a distinct legal regime: it may extend up to 200 nautical miles and gives the coastal State specified sovereign rights and jurisdiction while preserving specified rights and freedoms of other States. It is therefore not equivalent to sovereign territory. citeturn0search6

### Airspace
Store separately:
- sovereign airspace
- air-navigation authority
- FIR
- upper/lower limits where applicable
- ATS provider
- airspace classification
- international-airspace status
- effective dates

FIR must not be treated as synonymous with sovereignty. Air-navigation responsibility and territorial sovereignty are separate attributes.

## Entity roles

```text
SOVEREIGN
CLAIMANT
ADMINISTERING_AUTHORITY
JURISDICTION
MARITIME_AUTHORITY
AIRSPACE_AUTHORITY
AIR_NAVIGATION_SERVICE_PROVIDER
TREATY_PARTY
BOUNDARY_AGREEMENT_PARTY
```

One geographic area may have multiple roles and role values at the same time.

## Canonical schema

```text
TerritorialEntity
├── canonical_id
├── name
├── aliases
├── entity_type
├── geometry
├── centroid
├── country_or_jurisdiction
├── sovereign_status
├── claimant_entities[]
├── administering_authorities[]
├── jurisdiction_entities[]
├── legal_status
├── dispute_status
├── maritime_zones[]
├── airspace_records[]
├── boundary_records[]
├── treaty_records[]
├── effective_from
├── effective_to
├── source_records[]
└── provenance
```

## Maritime record

```text
MaritimeZone
├── zone_id
├── zone_type
├── coastal_state_or_states
├── baseline_reference
├── geometry
├── outer_limit
├── delimitation_agreement
├── deposited_chart_or_coordinates
├── legal_basis
├── effective_date
├── dispute_status
└── source_records[]
```

## Airspace record

```text
AirspaceRecord
├── airspace_id
├── geometry
├── sovereign_state
├── air_navigation_authority
├── FIR
├── ATS_provider
├── classification
├── vertical_limits
├── effective_date
└── source_records[]
```

## Source hierarchy

### Tier 1 — Primary international sources
- United Nations / DOALOS
- UN Treaty Collection
- UNCLOS and deposited charts/coordinates
- ICAO official material
- IHO official material

### Tier 2 — National primary sources
- foreign ministries
- maritime authorities
- hydrographic offices
- civil aviation authorities
- national boundary agencies
- official gazettes and legislation

### Tier 3 — Authoritative technical datasets
- recognized geospatial datasets
- navigation and aeronautical datasets
- treaty/boundary datasets

### Tier 4 — Secondary research
- academic publications
- reputable research institutions
- specialist geographic references

Secondary sources must not silently override a primary legal record.

## Boundary provenance
Each geometry should retain:

```text
source
source_type
retrieval_date
publication_date
legal_instrument
coordinate_reference_system
data_version
evidence_status
```

The UN DOALOS system specifically records deposited charts or lists of geographical coordinates for baselines and outer limits, making it a primary source for the maritime layer. citeturn0search0

## Dispute representation
Do not use a single `owner` field for disputed areas.

Use:

```text
claimed_by[]
administered_by[]
recognized_by[]
legal_basis[]
dispute_status
```

The UN maritime portal itself warns that displayed boundaries/names do not necessarily imply UN endorsement or acceptance and identifies examples where final status or boundaries remain unresolved. citeturn0search1

## Data quality states

```text
UNVERIFIED
OBSERVED
PRIMARY_SOURCE
CROSS_CHECKED
DISPUTED
OUTDATED
SUPERSEDED
INFERRED
```

A disputed boundary remains explicitly disputed rather than being converted to `VERIFIED` merely because a map displays it.

## GIS requirements
Use versioned geometries with:
- CRS / datum
- coordinate precision
- polygon/multipolygon geometry
- source geometry ID
- topology validation
- effective dates
- change history

## Integration

```text
Territory
 ↓
Country / Jurisdiction
 ├── Government
 ├── Banks
 ├── Companies
 ├── Exchanges
 ├── Payment Rails
 ├── Internet / Telecom
 ├── Infrastructure
 └── Regulatory Instruments

Territory
 ↓
Maritime Zone
 ↓
Ports / Shipping / Fisheries / Energy / Cables

Territory
 ↓
Airspace
 ↓
Airports / FIR / ATS / Aviation Infrastructure
```

## Safety and accuracy boundary
This registry is for geographic, legal, administrative, scientific and infrastructure knowledge. It does not provide military targeting, operational airspace exploitation, or tactical guidance.

## Implementation status
SPECIFICATION / DATA MODEL — v0.1

The schema is ready for ingestion. It does not claim that every global boundary, maritime claim or airspace polygon has already been ingested or independently verified.
