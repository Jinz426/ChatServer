# Global Exchange × Regulator × Main Board × Official Data Interface Registry v0.1

## Objective

Create a country-linked registry connecting securities regulators, exchange operators, main boards, issuer/security identifiers, official disclosures and lawful data interfaces. This is a source registry and normalization layer, not a trading system.

## Scope

For each jurisdiction, maintain:

- UN country identifier and ISO 3166 code
- securities regulator(s)
- exchange / market-infrastructure operator(s)
- cash-equity main board(s)
- other regulated boards and market segments
- central securities depository (CSD), central counterparty (CCP) and settlement infrastructure where applicable
- official issuer/listing directories
- official disclosure / filing portals
- official market-statistics portals
- official API, bulk-download, SFTP or other machine-readable interfaces where offered
- access requirements and authentication
- data licence / redistribution restrictions
- update frequency and last verification
- historical coverage and methodology

## Canonical relationship

```text
UN Country
  ↓
ISO 3166
  ↓
Jurisdiction
  ↓
Securities Regulator
  ↓
Exchange / Market Operator
  ↓
Main Board / Market Segment
  ↓
Issuer
  ↓
Security
  ↓
Ticker / ISIN / LEI / Local Identifier
  ↓
Official Filing / Market Data / Corporate Action
  ↓
CSD / CCP / Settlement
```

## Registry schema

```text
country_id
iso_alpha2
iso_alpha3
iso_numeric
jurisdiction_id
regulator_id
regulator_name
regulator_type
regulator_official_url
exchange_id
exchange_name
operator_name
operator_official_url
market_id
market_name
market_type
board_type
main_board_flag
listing_rules_url
issuer_directory_url
filing_portal_url
market_statistics_url
api_url
bulk_data_url
sftp_url
access_method
authentication_required
data_license
redistribution_allowed
historical_coverage
update_frequency
last_verified
source_status
notes
```

## Source authority levels

1. Official regulator
2. Official exchange / market operator
3. Official CSD / CCP / settlement provider
4. International standard-setting or statistical organization
5. Licensed commercial provider
6. Secondary source
7. AI inference

AI inference must never be represented as an official source.

## Identifier layer

Support, where applicable:

- ISO 3166 country identifiers
- ISO 4217 currency identifiers
- ISIN
- LEI
- exchange ticker / local security code
- MIC / market identifier code where available
- regulator-specific issuer identifiers

Keep identifiers in separate fields because one company/security may have multiple listings, classes and identifiers.

## Data-interface classes

```text
WEB_PORTAL
OFFICIAL_API
OFFICIAL_BULK_DOWNLOAD
OFFICIAL_SFTP
OFFICIAL_FILE_FEED
REGULATORY_FILING_FEED
WEBHOOK / EVENT_FEED
MANUAL_DOWNLOAD
NO_MACHINE_INTERFACE_FOUND
LICENSE_RESTRICTED
```

Do not scrape or redistribute data where terms, robots rules, authentication requirements or database rights prohibit it. Store source metadata and links even when the underlying dataset cannot legally be copied into the repository.

## Normalized market events

```text
LISTING
DELISTING
SUSPENSION
RESUMPTION
IPO
SECONDARY_OFFERING
STOCK_SPLIT
REVERSE_SPLIT
DIVIDEND
RIGHTS_ISSUE
MERGER
ACQUISITION
TENDER_OFFER
SPINOFF
BOARD_TRANSFER
SECURITY_CLASS_CHANGE
TRADING_RULE_CHANGE
REGULATORY_CHANGE
```

## International source anchors

### World Federation of Exchanges (WFE)

Use WFE membership and statistics as an international exchange/market-infrastructure cross-check. WFE states that it represents more than 250 exchanges and CCPs and publishes more than 350 market-data indicators. Its statistics portal provides monthly and annual indicators and time-series extraction for registered users. Source: https://www.world-exchanges.org/

### IOSCO

Use IOSCO as the international securities-regulator reference layer and for regulatory cooperation metadata. Regulator membership must be treated as a changing registry and verified against current IOSCO material rather than relying on old annual-report PDFs.

### World Bank WDI

Use WDI as an aggregate cross-country market-indicator source, including listed companies, market capitalization, value traded and turnover indicators. Do not treat WDI aggregates as replacements for exchange-level official records.

### IMF MFS / Financial Market Prices

Use IMF market-price and financial-market datasets for standardized international time series where applicable, preserving IMF definitions, reference periods and vintages.

## National adapter contract

Each country adapter should expose a common interface:

```text
get_regulator()
get_exchanges()
get_main_boards()
get_listed_issuers()
get_securities()
get_filings()
get_market_statistics()
get_corporate_actions()
get_identifier_mappings()
get_data_interface_metadata()
get_source_license()
get_last_update()
```

An adapter may return `NOT_PUBLIC`, `LICENSE_RESTRICTED`, `NOT_AVAILABLE` or `NOT_VERIFIED`; it must not fabricate missing data.

## Change detection

Monitor:

- official URL changes
- API/version changes
- board name changes
- regulator reorganizations
- exchange mergers/acquisitions
- listing-rule changes
- identifier changes
- data-schema changes
- discontinued feeds
- changed licensing terms

Store every change as an event with `observed_at`, `effective_at`, `source`, `old_value`, `new_value` and `verification_status`.

## Data-gap engine

For every jurisdiction calculate coverage for:

- regulator
- exchange
- main board
- issuer directory
- security identifiers
- filings
- market statistics
- corporate actions
- official interface
- licensing metadata

Statuses:

```text
COMPLETE
PARTIAL
STALE
CONFLICTING
NOT_PUBLIC
LICENSE_RESTRICTED
NOT_APPLICABLE
NOT_VERIFIED
```

## Cross-country dashboard dimensions

Compare jurisdictions by:

- number of regulated exchanges
- main-board listings
- listed-company count
- market capitalization
- turnover / liquidity
- IPO and delisting activity
- foreign-listing participation
- market-access characteristics
- disclosure infrastructure
- data-interface maturity
- CSD/CCP architecture
- regulatory coverage

All comparisons must preserve units, currencies, reference dates, methodology and source provenance.

## Initial global coverage plan

Seed the registry from WFE exchange/CCP membership and IOSCO regulator references, then verify each record against the relevant national regulator and exchange's official website. WFE membership is not equivalent to legal recognition in a jurisdiction, so the registry must retain both WFE status and national regulatory status as separate fields.

## Governance

The registry should be public-source oriented, auditable and versioned. It should not provide individualized investment advice, execute trades, bypass exchange access controls or redistribute restricted market data. It is intended to support research, economic analysis, interoperability and transparent source discovery.
