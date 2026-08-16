# Global Bank Registry v0.1

## Objective
Create a country-linked registry of banking institutions and official banking sources, complementing the existing country, currency, exchange, regulator, IMF and World Bank layers.

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

Do not assume that every country uses the same legal bank categories. Preserve the national legal classification and map it to a common ORBIT taxonomy.

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

## Data sources

### Primary sources
Prefer national central banks, banking supervisors, financial-services regulators, official bank registers, government registries and the banks' own official disclosures.

### International sources
- IMF Financial Access Survey (FAS)
- World Bank World Development Indicators (WDI)
- World Bank Global Financial Development Database (GFDD)
- BIS statistics where applicable
- IMF member financial data where applicable

IMF FAS provides annual statistics on financial-service access and usage and can distinguish provider types such as commercial banks, credit unions and microfinance institutions. The 2025 FAS release covers 163 economies and 121 series for 2004-2024. World Bank WDI also republishes indicators sourced from FAS, including commercial bank branches per 100,000 adults. These international datasets are aggregate/statistical layers and should not be treated as substitutes for a country's authoritative licensed-bank register.

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

## Change detection

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

Missing information must be labeled explicitly as `UNKNOWN`, `NOT_PUBLIC`, `NOT_APPLICABLE`, `STALE`, `CONFLICTING`, or `LICENSE_RESTRICTED`; never silently inferred.

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
