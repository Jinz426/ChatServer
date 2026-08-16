# IMF + Sovereign Currency Layer v0.1

## Purpose

Add IMF macro-financial data and country-level sovereign-currency metadata to the ORBIT financial-system model. This layer is a research/data-integration specification, not a claim that all currency or monetary information is real-time.

## Core entities

### Country monetary profile

Each country/economy profile should support:

- country / economy identifier
- ISO 3166-1 alpha-2 / alpha-3 where applicable
- IMF economy code where available
- currency name
- ISO 4217 currency code
- currency numeric code
- issuing monetary authority / central bank
- legal-tender status
- monetary regime
- exchange-rate arrangement
- currency union / shared-currency membership
- domestic-currency status
- official or reference exchange-rate source
- effective dates
- source and verification timestamp

Do not infer sovereignty solely from currency usage. A country may use another state's currency, share a currency, operate a currency board, or have other arrangements. Preserve legal and institutional distinctions.

## IMF datasets to integrate

### 1. World Economic Outlook (WEO)

Country-level historical and projected macroeconomic indicators, including:

- GDP and GDP growth
- GDP per capita
- PPP measures
- inflation
- unemployment
- current account
- government balance
- government debt
- trade
- commodity prices
- population

Store WEO vintage, reference period, publication date, methodology notes and whether a value is historical, estimated or projected. The IMF publishes WEO twice a year; the April 2026 dataset contains data from 1980 to the present and projections for most series for the following five years.

### 2. International Financial Statistics (IFS)

Where licensed/available through the IMF data service, ingest relevant monetary and financial statistics such as:

- monetary aggregates
- central-bank balance-sheet measures
- interest rates
- exchange rates
- international reserves
- selected banking indicators
- price indices

### 3. Balance of Payments / International Investment Position

Track:

- current account
- capital account
- financial account
- reserve assets
- direct investment
- portfolio investment
- other investment
- international investment position

### 4. Government Finance Statistics

Track public-sector and general-government fiscal information where available:

- revenue
- expenditure
- balance
- debt
- financing
- tax-related aggregates

### 5. Financial Access Survey

Where available, integrate access and usage indicators for financial services, including institutions, accounts, branches/ATMs and digital/mobile access.

### 6. Exchange-rate data

Store:

- representative rates
- currency units per SDR
- SDRs per currency unit
- observation date
- reporting institution
- source vintage

IMF representative rates are normally reported by the issuing central bank. Do not treat the IMF rate as an independent market price without recording the rate type and methodology.

### 7. AREAER

Integrate the IMF Annual Report on Exchange Arrangements and Exchange Restrictions, including:

- exchange-rate arrangement
- foreign-exchange market structure
- current-payment restrictions
- capital controls
- multiple-currency practices
- export/import payment rules
- nonresident/resident account restrictions
- relevant prudential measures
- country-specific effective dates where available

AREAER is especially important for understanding the difference between a currency's nominal exchange rate and the legal/operational environment governing its use.

### 8. IMF member / financial relationship layer

Where applicable, store:

- IMF membership status
- quota
- SDR allocation / holdings
- Fund arrangements
- outstanding IMF credit
- financial transactions
- reserve-related IMF information

These are institutional relationships and must not be interpreted as measures of a country's overall wealth.

## Sovereign-currency classification

ORBIT should classify currency relationships rather than using a simplistic "one country = one currency" rule.

Suggested values:

```text
DOMESTIC_SOVEREIGN_CURRENCY
SHARED_CURRENCY
CURRENCY_UNION
CURRENCY_BOARD
PEGGED_CURRENCY
MANAGED_FLOAT
FLOAT
OTHER_OFFICIAL_ARRANGEMENT
FOREIGN_CURRENCY_USED
MULTIPLE_CURRENCIES
NO_SEPARATE_CURRENCY
UNKNOWN
```

`DOMESTIC_SOVEREIGN_CURRENCY` should only be assigned when supported by authoritative legal/monetary sources. Currency issuance, legal tender and monetary sovereignty are distinct concepts and should be represented separately.

## Country monetary authority registry

```text
country_id
monetary_authority_id
authority_name
authority_type
jurisdiction
website
currency_codes
policy_rate_source
exchange_rate_source
reserve_source
legal_source
last_verified
```

The registry should link to official central-bank and finance-ministry sources rather than relying exclusively on international datasets.

## Financial-system graph

```text
Country
  ↓
Monetary Authority
  ↓
Currency
  ↓
Monetary Regime
  ↓
Exchange Arrangement
  ↓
Interest Rates / Money / Reserves
  ↓
Banks + Financial Institutions
  ↓
Capital Markets
  ↓
Fiscal System
  ↓
External Sector
  ↓
Households / Firms
  ↓
Real Economy
```

## Time-series model

Every observation should retain:

```text
indicator_id
country_id
currency_id
value
unit
frequency
reference_period
published_at
retrieved_at
vintage
source
methodology_version
status
```

Possible status values:

`OBSERVED`, `ESTIMATED`, `PROJECTED`, `REVISED`, `DISCONTINUED`, `MISSING`, `CONFLICTING`.

## Currency conversion layer

Conversions must preserve the original amount and rate:

```text
original_amount
original_currency
rate
rate_type
rate_date
converted_amount
conversion_currency
source
```

Do not overwrite local-currency values with USD conversions. Local prices, wages and financial balances must remain available in their original units.

## Data-quality and gap engine

For each country, detect missing or stale fields across:

- currency identity
- issuing authority
- exchange arrangement
- exchange rates
- inflation
- policy rate
- reserves
- money supply
- fiscal balance
- debt
- balance of payments
- financial access
- capital-flow restrictions
- IMF relationship data

The gap engine must distinguish genuinely unavailable data from data that is merely not yet ingested.

## Cross-country comparison

The comparison layer should support normalized views of:

- monetary regime
- inflation
- real and nominal exchange rates
- policy rates
- reserves
- government debt
- fiscal balance
- current account
- financial depth
- financial access
- capital-flow restrictions
- currency convertibility / exchange arrangements

Comparisons must preserve units, definitions, vintages and methodology. A ranking without those controls can be misleading.

## Source hierarchy

1. National central bank / monetary authority
2. National statistical office / finance ministry
3. IMF official datasets and publications
4. Other official international organizations
5. Licensed authoritative datasets
6. Secondary research sources

The IMF WEO is a macroeconomic analytical dataset; its historical estimates can differ from national official data and other IMF datasets. Preserve those distinctions.

## Live-data architecture

```text
Central Bank / Government
          ↓
     IMF / World Bank
          ↓
      Source Registry
          ↓
       Ingestion API
          ↓
  Validation + Versioning
          ↓
 Financial Knowledge Graph
          ↓
  Change Detection Engine
          ↓
     ORBIT Analytics
          ↓
 Country / Global Views
```

For real-time applications, supplement periodic IMF datasets with direct official central-bank feeds and other authorized sources. IMF WEO itself is published on a periodic cycle and should not be presented as a tick-by-tick market feed.

## Governance

- Respect IMF data terms, copyright and usage requirements.
- Keep source attribution and metadata.
- Do not redistribute restricted datasets without permission.
- Do not use the system to impersonate a central bank or regulator.
- Financial outputs are analytical information, not automatic financial advice or legal determinations.
- High-impact financial actions require appropriate human and regulatory controls.
