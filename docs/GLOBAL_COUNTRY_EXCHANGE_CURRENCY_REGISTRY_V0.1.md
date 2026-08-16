# Global Country, Exchange & Currency Registry v0.1

## Scope

Build a unified registry covering the 193 UN Member States, their exchange-market infrastructure, listed-market structures, financial regulators, securities identifiers, and currencies in circulation. The registry is designed as a metadata/integration layer; it does not itself grant legal authority, market-data redistribution rights, or financial licenses.

The UN currently has 193 Member States. The two UN non-member observer States (Holy See and State of Palestine) should be represented separately with `status=UN_OBSERVER_STATE`, not silently mixed into the 193-member baseline.

## Country registry

Required fields:

- `un_member_state`
- `un_admission_date`
- `un_name`
- `un_short_name`
- `iso_3166_alpha2`
- `iso_3166_alpha3`
- `iso_3166_numeric`
- `region`
- `subregion`
- `official_currency_relationships[]`
- `central_bank_or_monetary_authority[]`
- `financial_regulators[]`
- `securities_regulators[]`
- `exchange_operators[]`
- `main_boards[]`
- `data_sources[]`
- `last_verified`

## UN-country exchange registry

Map each country/economy to every relevant regulated exchange or trading venue:

- operator
- exchange name
- venue type
- jurisdiction
- country/economy relationship
- legal entity identifier where available
- main board
- secondary/SME/growth markets
- derivatives/fixed-income/commodity venues where applicable
- trading currency
- trading hours/time zone
- clearing counterparty
- central securities depository
- settlement cycle
- official source
- market-data licensing terms
- effective dates

Do not infer that every UN Member State has a domestic stock exchange or a main board. Record `none`, `shared`, `foreign_venue`, or `not_verified` explicitly.

## Exchange/operator registry

Normalize:

`operator → exchange → venue → market segment → board → instrument class`.

Store ownership/group relationships, legal jurisdiction, official website, regulator, source license and historical name changes.

## Main-board registry

For each main board, capture:

- board identifier
- exchange identifier
- listing eligibility
- issuer types
- securities admitted
- minimum capital/free-float requirements when officially documented
- disclosure/reporting rules
- trading mechanism
- currency
- market status
- effective dates
- official rulebook source

Rules are descriptive and must not be treated as legal advice.

## Regulator registry

Separate:

- securities regulator
- banking regulator
- central bank / monetary authority
- insurance regulator
- payments regulator
- financial-market infrastructure supervisor
- commodity-market regulator where applicable

Record jurisdiction, mandate, official source, legislation/rulebook source and verification date.

## Issuer / security identifier schema

Support, where legally and technically available:

- issuer_id
- legal_name
- LEI
- ISIN
- exchange_ticker
- local security identifier
- FIGI or other licensed identifier
- instrument_type
- share_class
- voting_rights
- currency
- primary_exchange
- listing_status
- country_of_issuer
- domicile
- effective_from / effective_until

Identifier systems are not interchangeable. Preserve the identifier authority and licensing terms for every field.

## Market statistics integration

### World Bank WDI

Ingest country-level stock-market indicators such as market capitalization, value traded, turnover, listed domestic companies and related indicators where available. Preserve the World Bank series code, source, reference year and vintage.

### WFE

Use World Federation of Exchanges aggregate data only where the applicable terms permit ingestion, storage and the intended display/redistribution. Preserve methodology, aggregation level and source license.

### IMF MFS / financial-market data

Ingest applicable IMF financial-market series with reference period, frequency, methodology, source institution and retrieval timestamp. Do not treat IMF representative exchange rates as a complete live market-price feed.

## Currency registry

The currency layer must cover more than sovereign currencies. Classify each currency-like unit as:

- sovereign/domestic currency
- shared currency
- currency union currency
- pegged/local currency
- foreign currency in official use
- parallel/commonly used currency where officially documented
- historical currency
- fund/unit of account
- precious-metal code
- digital currency / CBDC status
- virtual/digital asset (separate regulatory category)

Required currency fields:

- `currency_id`
- `iso_4217_alpha`
- `iso_4217_numeric`
- `currency_name`
- `minor_unit`
- `issuer`
- `monetary_authority`
- `legal_tender_status`
- `country_relationships[]`
- `shared_currency_group`
- `currency_regime`
- `circulation_status`
- `introduction_date`
- `withdrawal_date`
- `redenomination_history[]`
- `peg_reference`
- `central_bank_source`
- `last_verified`

ISO 4217 provides internationally recognized three-letter and three-digit currency/fund codes. The ISO standard also covers funds and precious metals, so ORBIT must distinguish those categories from legal tender.

## Exchange-rate layer

Store separately:

- official/representative rate
- central-bank reference rate
- market rate
- indicative rate
- mid rate
- bid/ask
- fixing
- SDR relationship

Required metadata:

`base_currency`, `quote_currency`, `rate`, `unit`, `timestamp`, `source`, `methodology`, `market_or_official`, `retrieved_at`, `vintage`.

IMF representative exchange rates are reported by issuing central banks for selected currencies and should remain clearly labeled as representative/official data rather than universal real-time market prices.

## Corporate-action normalization

Normalize:

- IPO
- secondary offering
- rights issue
- split
- reverse split
- dividend
- special dividend
- merger
- acquisition
- tender offer
- delisting
- suspension/resumption
- board transfer
- symbol change
- redenomination

Preserve source documents and effective dates.

## Market-data license registry

Every external dataset or feed must record:

- provider
- dataset
- license
- permitted use
- internal use
- public display
- redistribution
- caching
- derived-data rights
- attribution
- expiry/renewal
- API limits
- geographic restrictions

Never assume that publicly visible market data is freely redistributable.

## Time-series change detection

Detect:

- new exchange
- exchange rename/merger
- new main board
- board closure
- new currency
- currency withdrawal
- redenomination
- exchange-regime change
- regulator change
- issuer listing/delisting
- identifier change
- corporate action
- market-structure change
- source methodology change

Store both event and before/after snapshots.

## Financial-market data-gap engine

For each country/economy calculate coverage for:

- country identity
- exchange coverage
- regulator coverage
- main-board coverage
- issuer coverage
- security identifiers
- price history
- market statistics
- currency metadata
- exchange rates
- corporate actions
- licensing metadata

Gap statuses:

`COMPLETE`, `PARTIAL`, `STALE`, `CONFLICTING`, `NOT_APPLICABLE`, `NOT_PUBLIC`, `LICENSE_RESTRICTED`, `NOT_VERIFIED`.

## Cross-country comparison dashboard

Compare countries by:

- number/type of exchanges
- main-board structure
- listed issuers
- market capitalization
- liquidity
- turnover
- market capitalization/GDP
- listed companies/population or GDP
- currency regime
- exchange-rate regime
- financial-market access
- regulatory architecture
- data coverage
- data freshness

Do not rank countries solely by market size. Display methodology, reference period, missing values and data quality alongside every comparison.

## Recommended architecture

```text
UN 193 Member States
        ↓
Country Registry
        ├── Exchange / Operator Registry
        ├── Main-board Registry
        ├── Regulator Registry
        ├── Currency Registry
        └── Central-bank Sources
                 ↓
        Securities / Issuer Graph
                 ↓
      WDI / WFE / IMF / National Data
                 ↓
      Time-series + Corporate Actions
                 ↓
       Provenance + License Layer
                 ↓
        Data-gap / Change Engine
                 ↓
       Cross-country Dashboard
```

## Source baseline

Primary reference families:

- United Nations Member States
- ISO 3166 country codes
- ISO 4217 currency codes
- World Bank WDI
- World Bank GFDD / Global Findex where relevant
- IMF financial-market and exchange-rate datasets
- World Federation of Exchanges where licensed
- National exchanges
- National securities regulators
- Central banks / monetary authorities

The registry should store source URLs, retrieval timestamps, dataset versions and methodology references. Official sources take priority over secondary summaries.
