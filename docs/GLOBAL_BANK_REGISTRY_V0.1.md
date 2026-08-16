# Global Bank Registry v0.2

## Objective
Create a country-linked registry of banking institutions and official banking sources, complementing the country, currency, exchange, regulator, IMF and World Bank layers.

## Scope
For each UN member country, maintain a normalized registry for:
- Central bank / monetary authority
- Commercial banks / deposit-taking banks
- State-owned or public-sector banks
- Development banks
- Cooperative / mutual banks where officially recognized
- Savings banks
- Islamic banks where applicable
- Microfinance institutions where included by the national framework
- Digital banks / neobanks where licensed
- Foreign-bank branches and subsidiaries where publicly registered
- Specialized banks and other regulated deposit-taking institutions

Do not assume every country uses the same legal bank categories. Preserve national legal classification and map it to a common ORBIT taxonomy.

## Institution schema
```text
bank_id
country_iso_3166_1
jurisdiction
legal_name
common_name
institution_type
legal_form
ownership_type
license_status
regulator_id
central_bank_id
parent_group_id
foreign_parent_country
headquarters_city
official_website
official_registry_url
license_url
annual_report_url
financial_statements_url
api_url
open_data_url
swift_bic_if_public
lei_if_public
currency
reporting_frequency
established_date
license_effective_from
license_effective_until
last_verified
source_authority
source_url
source_license
status
```

## Institution types
```text
CENTRAL_BANK
COMMERCIAL_BANK
STATE_BANK
DEVELOPMENT_BANK
SAVINGS_BANK
COOPERATIVE_BANK
MUTUAL_BANK
ISLAMIC_BANK
MICROFINANCE_BANK
DIGITAL_BANK
SPECIALIZED_BANK
FOREIGN_BANK_BRANCH
FOREIGN_BANK_SUBSIDIARY
OTHER_REGULATED_DEPOSIT_TAKER
```

## Regulatory relationship
```text
Country
  ↓
Monetary Authority / Central Bank
  ↓
Banking Regulator (if separate)
  ↓
Licensed Institution
  ↓
License / Registration
  ↓
Branches / Service Points
  ↓
Products / Accounts / Credit
```

## Source hierarchy
1. National central bank / monetary authority
2. National banking supervisor / financial-services regulator
3. Official government or company registry
4. Official bank disclosure
5. International statistical sources
6. Other authoritative sources with explicit provenance

A national regulator's current licensing record takes precedence over an aggregate international dataset when the two answer different questions.

## Data sources
### Primary sources
Prefer national central banks, banking supervisors, financial-services regulators, official bank registers, government registries and banks' official disclosures.

### International sources
- IMF Financial Access Survey (FAS)
- World Bank World Development Indicators (WDI)
- World Bank Global Financial Development Database (GFDD)
- World Bank Global Findex
- BIS statistics where applicable
- IMF member financial data where applicable

International datasets are statistical/context layers and must not be treated as substitutes for a country's authoritative licensed-bank register.

## Country coverage workflow
For every country, create a source record before institution ingestion:
```text
COUNTRY
 → CENTRAL_BANK_SOURCE
 → BANK_REGULATOR_SOURCE
 → LICENSED_BANK_REGISTER_SOURCE
 → OFFICIAL_BANK_SOURCES
 → FINANCIAL_DATA_SOURCES
 → API/OPEN_DATA_SOURCES
```

Coverage states:
```text
DISCOVERED
SOURCE_VERIFIED
PARTIALLY_INGESTED
FULLY_INGESTED
STALE
CONFLICTING
NOT_PUBLIC
NOT_AVAILABLE
LICENSE_RESTRICTED
```

"FULLY_INGESTED" means the authoritative public register available to the project has been processed and validated; it does not mean every private banking record exists.

## Branch / access layer
Track, where officially available:
- Number of institutions
- Number of branches
- ATMs
- Agents / service points
- Deposit accounts
- Loan accounts
- Outstanding deposits
- Outstanding loans
- Digital accounts / e-money where defined
- Gender-disaggregated access where lawfully and appropriately published
- Household / SME access where available

## Time and evidence
Every record must retain:
```text
observed_at
published_at
retrieved_at
effective_from
effective_until
last_verified
source_version
methodology_version
evidence_reference
confidence
```

Institution status should support:
```text
ACTIVE
LICENSED
SUSPENDED
RESTRICTED
RESOLVED
MERGED
ACQUIRED
RENAMED
REVOKED
CLOSED
UNKNOWN
```

## Historical change detection
Detect and record:
```text
BANK_LICENSE_GRANTED
BANK_LICENSE_REVOKED
BANK_OPENED
BANK_CLOSED
BANK_MERGED
BANK_ACQUIRED
BANK_RENAMED
BANK_CONVERTED
BANK_OWNERSHIP_CHANGED
REGULATOR_CHANGED
WEBSITE_CHANGED
REGISTRY_UPDATED
```

Historical records must never overwrite earlier observations. Use effective dates and versioned snapshots.

## Identifier crosswalks
Where publicly available, map:
- ISO country codes
- Bank canonical ID
- Legal-entity identifiers (LEI)
- SWIFT/BIC
- National license/registration number
- Securities ticker / exchange identifiers for listed institutions
- Parent-group identifiers

Identifier mappings must preserve source and confidence because different identifiers can refer to different legal entities, branches or historical entities.

## Data-gap engine
For each country calculate coverage for:
- Central bank
- Banking regulator
- Licensed-bank register
- Bank websites
- License records
- Branch network
- ATM/service-point data
- Deposits
- Loans
- Digital banking
- Ownership
- Financial statements
- API/open-data availability
- Historical status

Missing information must be labeled explicitly as `UNKNOWN`, `NOT_PUBLIC`, `NOT_APPLICABLE`, `STALE`, `CONFLICTING`, or `LICENSE_RESTRICTED`; never silently inferred.

## Quality controls
Before an institution is marked verified:
1. Resolve canonical legal identity.
2. Confirm jurisdiction.
3. Confirm authoritative source.
4. Confirm current or historical license status.
5. Record effective dates where available.
6. Preserve source URL and retrieval timestamp.
7. Check duplicate/alias records.
8. Compare relevant international statistics without overriding the regulator.
9. Record conflicts instead of silently choosing a value.
10. Run schema and identifier validation.

## Privacy and security
This registry is limited to public institutional, regulatory and aggregate financial information. Never ingest customer account data, balances, credentials, KYC files, private transaction records or other confidential banking information.

## Integration with ORBIT
```text
UN Country
 ↓
ISO Codes
 ↓
Sovereign Currency
 ↓
Central Bank
 ↓
Bank Regulator
 ↓
Licensed Banks
 ↓
Exchange / Listed Issuers
 ↓
IMF / World Bank Financial Indicators
 ↓
Companies / Industry / Land / Resources
 ↓
Global Economic Knowledge Graph
```

## Governance
Bank lists and licensing information can be legally sensitive or rapidly changing. Use authoritative public sources, respect source licenses and terms of use, preserve citations/provenance, and do not infer whether an institution is currently licensed when the authoritative registry cannot verify it.

## Implementation roadmap
Phase 1 — Canonical schemas and country/source registry.
Phase 2 — Official regulator and bank-register ingestion.
Phase 3 — Identifier resolution and historical status.
Phase 4 — Financial indicators and access statistics.
Phase 5 — Automated source health checks, re-verification and data-gap monitoring.

## Completion rule
A country is not marked COMPLETE merely because a bank list exists. Completion requires a validated authoritative source, canonical entities, license/status provenance, temporal versioning, quality checks and documented access/licensing conditions.
