# World Bank Financial Data Integration v0.2

This specification expands the ORBIT financial-system layer into a structured ingestion, metadata, comparison and change-detection pipeline.

## Scope

The integration covers:

1. World Bank Financial System Layer specification
2. Country-level GFDD ingestion
3. Global Findex 2025 ingestion
4. WDI financial-sector indicator ingestion
5. Indicator metadata registry
6. Country financial profiles
7. Central-bank / regulator source registry
8. Financial-system visualization
9. Time-series change detection
10. Financial data-gap engine
11. Cross-country financial-system comparison

## Authoritative source families

### Global Financial Development Database (GFDD)

Use GFDD as the historical financial-system structure layer. The current World Bank dataset page describes 214 economies, annual data beginning in 1960, 108 indicators, and data through 2021 in the September 2022 release. It uses a 4x2 framework: depth, access, efficiency and stability across financial institutions and financial markets.

Source: https://www.worldbank.org/en/publication/gfdr/data/global-financial-development-database

### Global Findex 2025

Use the 2025 release for financial inclusion and digital connectivity. It is based on nationally representative surveys of about 148,000 adults in 141 economies conducted during 2024. The release provides almost 300 indicators covering accounts, payments, saving, borrowing, financial resilience, mobile-phone ownership, internet use and digital safety, with breakdowns including gender, income, labor-force participation, age and rural/urban residence.

Sources:
- https://www.worldbank.org/en/publication/globalfindex/report
- https://www.worldbank.org/en/publication/globalfindex/download-data
- https://www.worldbank.org/en/publication/globalfindex/methodology

### World Development Indicators (WDI)

Use WDI for broader macroeconomic and development context, including financial-sector, debt, financial-flow and related indicators. The World Bank DataBank currently lists WDI as updated July 13, 2026. WDI is compiled from officially recognized international sources and provides national, regional and global estimates.

Source: https://databank.worldbank.org/

## Data model

Every observation should contain, where available:

```text
indicator_id
indicator_name
country_code
country_name
jurisdiction
period
value
unit
frequency
source_dataset
source_url
source_provider
source_version
published_at
retrieved_at
methodology_version
status
confidence
notes
```

## Indicator metadata registry

The registry must preserve the World Bank indicator identifier and canonical definition rather than inventing a new meaning. Suggested fields:

```text
indicator_id
canonical_name
short_name
description
source_dataset
topic
subtopic
institution_or_market
framework_dimension
data_type
unit
frequency
coverage_start
coverage_end
methodology
source_provider
source_url
license_or_terms
last_verified
```

## Country financial profile

Each country profile should aggregate, but not overwrite, the source observations.

```text
Country
├── Financial institutions
│   ├── Depth
│   ├── Access
│   ├── Efficiency
│   └── Stability
├── Financial markets
│   ├── Depth
│   ├── Access
│   ├── Efficiency
│   └── Stability
├── Financial inclusion
├── Digital finance
├── Payments
├── Saving
├── Borrowing
├── Financial resilience
├── Debt / financial flows
└── Regulatory ecosystem
```

Derived scores must retain their formula, input indicators and version. They must never replace the underlying source data.

## Central-bank / regulator source registry

For every country, maintain a source registry for relevant authorities, such as:

```text
central_bank
banking_regulator
securities_regulator
insurance_regulator
payment_regulator
financial_intelligence_authority
deposit_insurance
pension_regulator
consumer_finance_authority
stock_exchange
official_statistics_office
finance_ministry
```

Fields:

```text
country_code
institution_name
institution_type
jurisdiction
official_domain
official_data_portal
api_or_download_url
regulatory_scope
language
last_verified
status
```

This registry is a routing layer, not a claim that every country uses the same institutional structure.

## Ingestion pipeline

```text
World Bank source
      ↓
Download / API
      ↓
Raw immutable snapshot
      ↓
Schema validation
      ↓
Country-code normalization
      ↓
Indicator metadata mapping
      ↓
Unit / frequency validation
      ↓
Observation store
      ↓
Country financial profiles
      ↓
Visualization / comparison
```

Never overwrite raw source snapshots. Store new releases as new versions.

## Time-series change detection

Detect:

- new observation
- revised observation
- missing observation
- methodology change
- structural break
- unusually large movement
- country coverage change

Every detected change should link to the source release and methodology version. Statistical anomaly detection is a research aid, not an automatic claim of fraud or causation.

## Financial data-gap engine

Calculate completeness separately by dataset and indicator family:

```text
country
├── GFDD completeness
├── Findex completeness
├── WDI financial completeness
├── regulator-source completeness
├── time coverage
├── metadata completeness
└── freshness
```

A gap should be classified as one of:

`NOT_AVAILABLE`, `NOT_PUBLISHED`, `OUTDATED`, `MISSING_METADATA`, `COUNTRY_MAPPING_UNCERTAIN`, `SOURCE_UNAVAILABLE`, `CONFLICTING`, `PENDING_VALIDATION`.

## Financial-system visualization

Planned views:

- country financial-system profile
- GFDD 4x2 matrix
- Findex inclusion dashboard
- WDI financial indicators timeline
- country comparison matrix
- regional map
- time-series charts
- financial-data coverage map
- regulator/source map

Charts must preserve source, unit, period and methodology metadata.

## Cross-country comparison

Comparisons should support:

```text
country × indicator × year
country × GFDD dimension
country × financial inclusion
country × digital finance
country × financial stability
country × financial access
country × financial market depth
```

Do not rank countries using a composite score unless the weighting method is explicit, reproducible and versioned.

## Important data freshness rule

World Bank datasets do not all update at the same frequency. GFDD's current published release is historical through 2021, while WDI is updated more frequently and Global Findex 2025 contains survey data collected in 2024. Therefore the system must expose `reference_period` and `retrieved_at` separately and must never label all World Bank financial data as real-time.

## Licensing and responsible use

Store source attribution and applicable dataset terms. Do not redistribute raw data beyond the permissions of the source. Preserve original definitions and methodological notes. Use official regulator sources for current legal requirements instead of treating historical World Bank indicators as legal advice.

## Roadmap

- [ ] GFDD country ingestion adapter
- [ ] Global Findex 2025 country ingestion adapter
- [ ] WDI financial-sector query adapter
- [ ] unified country-code registry
- [ ] indicator metadata registry
- [ ] country financial profile generator
- [ ] regulator source registry
- [ ] visualization layer
- [ ] time-series change detector
- [ ] financial data-gap engine
- [ ] cross-country comparison engine
- [ ] automated source freshness monitor
