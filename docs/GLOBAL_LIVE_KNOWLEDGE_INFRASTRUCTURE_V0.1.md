# Global Live Knowledge Infrastructure v0.1

## Purpose

Extend ORBIT from a static knowledge repository into a continuously updated, evidence-aware world model. The system should represent **space, time, people, objects, resources, economy, infrastructure, regulation and AI capabilities** while preserving provenance, uncertainty, permissions and change history.

## Core model

```text
Real World
   ↓
Data Sources
   ↓
Ingestion
   ↓
Normalization
   ↓
Validation / Provenance
   ↓
Knowledge Graph
   ↓
AI Reasoning
   ↓
Applications / Decisions
   ↺
```

## 15 layers

### 1. Time
Every changing record should support effective_from, effective_until, observed_at, published_at, verified_at, source_version and status.

### 2. Real-time events
Examples: price_changed, law_changed, license_changed, factory_opened, factory_closed, road_changed, building_abandoned, population_changed, shipment_moved, disaster and resource_status_changed.

### 3. Provenance / evidence
Every important observation should retain source, collection method, timestamp, original evidence reference, transformations, model processing and conclusion.

### 4. Confidence
Use explicit states such as OBSERVED, CONFIRMED, REPORTED, INFERRED, ESTIMATED, CONFLICTING and UNKNOWN. Confidence must not be confused with truth.

### 5. Spatial hierarchy
Country → jurisdiction → city → neighborhood → parcel → building → floor → unit → business → product, plus road, rail, metro, bus, bicycle, pedestrian, port and airport networks.

### 6. Industry / supply chain
Track resource → material → component → factory → warehouse → transport → distributor → retailer → consumer → waste → recovery → secondary material.

### 7. Resource layer
Track land, water, agriculture, forests, minerals, energy, fisheries, livestock, biodiversity and recyclable materials. Distinguish AVAILABLE, RESERVED, PROTECTED, DEPLETED, REGENERATING and UNDER_DEVELOPMENT where supported by evidence.

### 8. Population / human needs
Represent population, age bands, households, occupations, skills, education, mobility, housing, food, energy, healthcare and transport demand at appropriate aggregate levels. Avoid unnecessary personal identification data.

### 9. Prices / economy
Connect retail and wholesale prices to currency, exchange rates, inflation, purchasing power, wages, energy, land, logistics, taxes and documented supply-chain costs.

### 10. Workforce
Compare skills and training capacity with verified local labor demand. Outputs should support planning rather than automatically making employment decisions about individuals.

### 11. Infrastructure capacity
Track roads, water, electricity, internet, schools, hospitals, warehouses, ports, rail, housing and waste-processing capacity, including capacity, utilization and maintenance status when available.

### 12. Circular economy
Model product lifecycles and material flows from production through consumption, sorting, recovery, recycling and secondary production.

### 13. Regulatory engine
Country → jurisdiction → activity → regulation → license/permit/registration/approval → regulator → application → inspection/reporting → expiration. Regulatory records must include official sources and verification dates.

### 14. Identity and permissions
Separate human, organization, AI, device and data identities. Permissions should be explicit and scoped: READ, WRITE, ANALYZE, EXPORT, SHARE, PAY, EXECUTE and DELETE. No unrestricted device or account access.

### 15. Multi-agent AI
AI agents should have explicit identities, capabilities, costs, permissions, evidence requirements and responsibility scopes. Model interoperability does not imply unrestricted model-to-model training or data sharing.

## Data Gap Engine

The system should measure what is missing, stale or contradictory rather than pretending the world is complete.

```text
Country / Region
  ├─ Population completeness
  ├─ Roads completeness
  ├─ Buildings completeness
  ├─ Business completeness
  ├─ Price completeness
  ├─ Supply-chain completeness
  ├─ Regulatory completeness
  └─ Recycling-flow completeness
```

A gap record should contain `entity`, `field`, `jurisdiction`, `priority`, `last_known_value`, `missing_reason`, `requested_source`, `last_verified` and `confidence`.

## Update strategy

Prefer event-driven updates where sources support them. Otherwise use scheduled refreshes with source-specific frequencies. Store snapshots and change events so historical states can be reconstructed.

## Source hierarchy

Prefer, in order appropriate to the subject:

1. Official government / regulator sources
2. Primary organization or operator sources
3. Licensed authoritative datasets
4. Reputable research / statistical sources
5. Carefully labeled community observations
6. AI-generated inference only as inference, never as primary evidence

## Safety and governance

- Do not expose private personal data without authorization.
- Do not infer sensitive personal attributes from ordinary observations.
- Do not turn confidence scores into legal, medical or financial certainty.
- Preserve source attribution and applicable licenses.
- Respect robots.txt, API terms, rate limits and database rights where applicable.
- Human review is required for high-impact regulatory, financial, employment, medical or safety decisions.

## Roadmap

- [ ] Event schema
- [ ] Temporal schema
- [ ] Provenance schema
- [ ] Data-gap schema
- [ ] Source registry
- [ ] Refresh scheduler
- [ ] Change detector
- [ ] Conflict resolver
- [ ] Knowledge graph storage
- [ ] Regulatory rule engine
- [ ] GIS connector layer
- [ ] Public dashboard
- [ ] User-controlled private knowledge layer
