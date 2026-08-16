# Global Database Update v0.2

## Objective

Unify the project into a provenance-aware global economic and infrastructure knowledge system. This update consolidates the layers developed so far and defines the next ingestion boundary.

## Canonical country universe

- Base country registry: 193 UN Member States.
- Preserve UN observer states separately rather than silently mixing them into the 193-member count.
- Use ISO country codes as normalization keys where applicable.
- Never infer sovereignty, borders, or legal status solely from a map dataset.

## Global source layers

### 1. International organizations

- United Nations: country/member-state reference
- ISO: country, currency, language, date/time and other standards
- World Bank: WDI, GFDD and Global Findex
- IMF: WEO, IFS, MFS, FAS, balance of payments, government finance and exchange-rate datasets
- WIPO: patents, trademarks, industrial designs, geographical indications and IP statistics
- WFE: exchange and market aggregates where licensed
- IOSCO: securities-regulator / market-infrastructure reference material
- BIS: banking and monetary statistics where applicable
- WTO: trade and tariff reference data where applicable

### 2. Country official-source registry

For every country, maintain source records for:

- Government portal
- Parliament / legislation
- National statistics office
- Ministry of finance
- Tax authority
- Central bank / monetary authority
- Banking regulator
- Securities regulator
- Insurance / pension regulator
- Payment-system regulator
- Stock exchange(s)
- Central securities depository / clearing infrastructure where applicable
- Company / business registry
- Land / cadastral authority where public
- Mapping / GIS authority where public
- Agriculture / natural-resource agencies
- Trade / customs authority
- Industry / factory authority
- Product standards authority
- Environmental authority
- Public procurement source
- Official open-data portal

### 3. Financial-system registry

Country → currency → monetary authority → banking regulator → banks → payment systems → financial markets → exchanges → listed issuers → securities → clearing/settlement.

### 4. Capital-market registry

Country → regulator → exchange/operator → market segment → main board → issuer → security identifier → filings → market statistics → corporate actions → settlement infrastructure → official data interface.

Identifiers may include ISO 3166, ISO 4217, ISIN, LEI, MIC, local security identifiers and regulator/company identifiers when officially available.

### 5. Banking registry

Track central banks, licensed commercial banks, state-owned banks, development banks, savings/cooperative institutions, Islamic banks, digital banks, foreign-bank branches/subsidiaries and other jurisdiction-specific licensed institutions.

Record legal name, regulator, license status, effective dates, parent group, headquarters, official website, official registry entry, reporting source, data interface and historical changes where public.

### 6. Currency registry

Track circulating and historical currencies separately. Record currency code, numeric code, name, issuer/monetary authority, legal-tender status, shared-currency status, currency union, exchange-rate regime, redenomination history, replacement currency, official exchange-rate sources and CBDC status where officially documented.

### 7. Real economy / infrastructure registry

- Land: available, reserved, protected, developed and regeneration status
- Housing: apartment, landed housing, village, mixed-use and other built forms
- Commercial: shops, markets, malls, warehouses
- Industry: factories and production clusters
- Agriculture: farms, livestock and food-production areas
- Transport: pedestrian, bicycle, motorcycle, car, truck, bus, tram, rail and metro networks
- Utilities: electricity, water, waste, telecommunications
- Resources: water, energy, minerals, forestry, fisheries and recyclable materials

### 8. Product / supply-chain registry

Resource → material → component → factory → warehouse → logistics → distributor → retailer → consumer → waste → sorting → recovery → secondary material.

Product observations may include price, unit, quantity, quality indicators, packaging, origin, manufacturer, brand, standards and IP references when reliably identified.

### 9. IP / technology registry

Company/product/technology relationships may link to WIPO-derived patent, trademark, design and geographical-indication records. Keep rights, jurisdictions, status and dates separate from technical inference.

## Common source record

```text
source_id
country_code
jurisdiction
organization
organization_type
domain
official_url
dataset_url
api_url
access_method
license_status
redistribution_status
coverage
language
update_frequency
last_checked
last_published
source_version
methodology_version
status
```

## Common observation record

```text
entity_id
indicator_id
value
unit
currency
reference_period
observed_at
published_at
retrieved_at
source_id
source_version
methodology_version
confidence
observation_status
provenance
```

## Data quality states

`COMPLETE`, `PARTIAL`, `STALE`, `CONFLICTING`, `NOT_APPLICABLE`, `NOT_PUBLIC`, `LICENSE_RESTRICTED`, `NOT_VERIFIED`.

AI inference must never be silently stored as an official observation.

## Update pipeline

```text
Official / licensed sources
        ↓
Source registry
        ↓
Scheduled/API ingestion
        ↓
Schema normalization
        ↓
Identifier resolution
        ↓
Temporal validation
        ↓
Provenance validation
        ↓
Conflict detection
        ↓
Data-gap engine
        ↓
Knowledge graph / time series
        ↓
Comparison + visualization
```

## Time-series change detection

Detect additions, removals, revisions, renamed entities, changed definitions, changed methodologies, stale sources, changed URLs/APIs, corporate actions, license changes and regulatory changes. Preserve historical versions instead of overwriting them.

## Data-gap engine

For each country and domain calculate coverage states for:

- population
- land / GIS
- buildings
- roads / mobility
- businesses
- factories
- agriculture
- banks
- currencies
- exchanges
- regulators
- listed issuers
- securities
- prices
- macroeconomics
- trade
- IP
- licenses
- resources
- recycling / circular economy

The gap engine should identify missing, stale, conflicting or license-restricted data and recommend an authoritative source rather than inventing a value.

## Cross-country comparison

Comparison dimensions should include data definitions, units, currencies, purchasing-power context, reference periods, population denominators, coverage, methodology and source authority before ranking or aggregation.

## License and access rules

Official availability does not automatically mean unrestricted redistribution. Store source terms, API restrictions, attribution requirements and redistribution status. For licensed market data, store metadata and permitted references rather than copying restricted datasets into the repository.

## Current ingestion boundary

This repository currently contains the architecture/specification layers for the global system. Full 193-country, exchange-by-exchange, bank-by-bank and dataset-by-dataset population is a continuing ingestion program; it should be performed through the source adapters with validation and provenance rather than represented as complete before the records are actually verified.

## Immediate next ingestion batches

1. UN 193 country master + ISO mappings
2. Country official-source registry
3. Central-bank / banking-regulator registry
4. Exchange / regulator / main-board registry
5. Currency master + historical currency relationships
6. World Bank WDI source/indicator catalog
7. IMF dataset/source catalog
8. WIPO source and IP-statistics catalog
9. WFE/market-data licensed-source registry
10. Per-country data-gap report
