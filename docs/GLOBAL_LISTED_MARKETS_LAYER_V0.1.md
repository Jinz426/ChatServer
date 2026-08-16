# Global Listed Markets Layer v0.1

## Purpose

Create a country- and exchange-level registry for listed equity markets, primary/main boards, secondary boards, market operators, listed issuers, securities, market structure, trading, clearing, settlement, ownership, disclosures and historical changes.

This is a **data architecture specification**, not a claim that every field is currently available for every country. Source coverage and licensing must be recorded explicitly.

## Core hierarchy

```text
UN / Country
  ↓
Jurisdiction
  ↓
Market regulator
  ↓
Exchange group / market operator
  ↓
Exchange
  ↓
Market segment / Main Board / Primary Market / Growth Market
  ↓
Issuer
  ↓
Security / Share class / ISIN where lawfully available
  ↓
Trading / clearing / settlement
  ↓
Price / volume / market value / corporate actions
```

## Country-level fields

- Country and ISO codes
- Jurisdiction and regulator
- Legal framework
- Exchange(s) serving the jurisdiction
- Main/primary board name
- Other equity boards and market segments
- Listing eligibility
- Listing requirements
- Disclosure requirements
- Accounting/reporting standards
- Foreign issuer rules
- Foreign ownership restrictions
- Market access rules
- Trading calendar and sessions
- Settlement cycle
- Clearing model / CCP
- Central securities depository
- Investor protection framework
- Short selling / securities lending rules where applicable
- Capital controls and relevant exchange restrictions
- Tax treatment of securities transactions where available
- Official source URLs and verification timestamps

## Exchange-level fields

- Legal entity
- Exchange name and identifiers
- Parent / group
- Country and location
- Market segments
- Main board
- Growth / SME / alternative markets
- Listing count
- Domestic vs foreign listings
- Market capitalization
- Value traded
- Number of trades
- Turnover
- Trading volume
- New listings / delistings
- IPO activity
- ETF / bond / derivative products where applicable
- Trading hours
- Currency
- Clearing and settlement links
- Regulatory status
- Historical ownership / structural changes

The World Federation of Exchanges describes itself as the global industry association for exchanges and clearing houses and publishes hundreds of market-data indicators. Its statistics should be treated as an important aggregate source, while exchange and regulator sources remain necessary for detailed market-level records. citeturn0search13

## Issuer-level fields

Where lawful and available:

- Legal issuer name
- Trading symbol(s)
- Exchange
- Board / segment
- ISIN and other official identifiers
- Country of incorporation
- Listing jurisdiction
- Primary listing
- Secondary / cross-listings
- Security class
- Shares outstanding
- Free float
- Market capitalization
- Listing date
- Delisting date/status
- Sector / industry classification
- Revenue
- Profit / loss
- Assets / liabilities
- Cash flow
- Dividend history
- Corporate actions
- Ownership disclosures
- Related-party disclosures
- Annual/interim reports
- Material announcements
- Auditor
- Governance information
- Official issuer filings

## Security-level fields

- Instrument type
- Share class
- ISIN where permitted
- Ticker
- Currency
- Face/reference values where applicable
- Shares outstanding
- Voting rights
- Listing status
- Trading status
- Primary exchange
- Market segment
- Corporate-action history

## Market-data layer

Store separate observations for:

- Open
- High
- Low
- Close
- Adjusted close where legitimately sourced
- Volume
- Turnover value
- Bid/ask when licensed
- Market capitalization
- Number of trades
- Volatility measures
- Index membership
- Index level / return

Do not assume real-time market data is freely redistributable. Record data-license, entitlement and redistribution restrictions for every provider.

## Corporate-action layer

Track:

- IPO
- Follow-on offering
- Rights issue
- Stock split
- Reverse split
- Bonus issue
- Dividend
- Spin-off
- Merger
- Acquisition
- Tender offer
- Delisting
- Suspension / resumption
- Symbol change
- Board transfer
- Share-class conversion

## Global benchmark indicators

Connect to World Bank WDI indicators sourced from WFE, including:

- Market capitalization of listed domestic companies
- Market capitalization as % of GDP
- Listed domestic companies, total
- Stocks traded, total value
- Stocks traded as % of GDP
- Turnover ratio
- S&P Global Equity Indices annual change

The World Bank currently shows these stock-market indicators with WFE as source, with series extending through 2025 for several indicators. citeturn0search2turn0search7

World Bank metadata defines listed domestic companies as companies with shares listed on an exchange at year-end, with specific exclusions and methodology. citeturn0search4

## IMF connection

Connect country-level equity-market observations to IMF Monetary and Financial Statistics Financial Market Prices where appropriate. IMF states that this dataset contains country-specific share-price information and warns that national methodologies are not standardized across countries; ORBIT must therefore preserve methodology metadata instead of treating all observations as perfectly comparable. citeturn0search0

## Main-board registry

For every country with an equity market, create a record where available:

```yaml
country:
exchange:
market_operator:
regulator:
main_board:
other_boards: []
listing_requirements_source:
market_rules_source:
issuer_disclosure_source:
market_data_source:
clearing_source:
settlement_source:
last_verified:
data_license:
coverage_status:
```

## Time-series and change detection

Every record should support:

- observation date
- publication date
- retrieval date
- source version
- methodology version
- previous value
- current value
- detected change
- corporate/regulatory event link
- confidence

The system should distinguish a genuine market event from a data revision, restatement, symbol change, exchange migration or methodology change.

## Data-gap engine

For each country/exchange, calculate coverage for:

- Exchange identity
- Main-board identity
- Regulator
- Listing rules
- Issuer universe
- Security identifiers
- Market capitalization
- Trading activity
- Corporate actions
- Financial filings
- Ownership
- Clearing
- Settlement
- Historical observations
- Real-time entitlement

Example:

```text
Thailand
  Exchange identity       COMPLETE
  Main board              COMPLETE
  Regulator               COMPLETE
  Issuer universe         PARTIAL
  Intraday prices         LICENSED / RESTRICTED
  Corporate actions       PARTIAL
  Historical data         COMPLETE/PARTIAL by source
```

## Comparison layer

Compare countries on:

- Number of listed companies
- Market capitalization / GDP
- Liquidity
- Turnover
- New listings
- Delistings
- Foreign listings
- Market concentration
- Sector concentration
- Market access
- Settlement infrastructure
- Regulatory structure
- Investor participation
- Market stability

Comparisons must preserve source methodology and should not produce a simplistic ranking when definitions differ. World Bank metadata explicitly notes that cross-country comparability can be limited by reporting, accounting and methodological differences. citeturn0search9

## Real-time architecture

```text
Official exchange / regulator feeds
             ↓
Licensed market-data providers
             ↓
Filings / corporate actions
             ↓
Normalization
             ↓
Identifier resolution
             ↓
Provenance + license checks
             ↓
Time-series store
             ↓
Knowledge graph
             ↓
ORBIT analytics
```

## Governance

- Never scrape or redistribute restricted market data in violation of provider terms.
- Prefer official exchange/regulator filings for legal and issuer facts.
- Separate public historical statistics from licensed real-time feeds.
- Preserve source attribution and data-license metadata.
- Do not treat market information as personalized investment advice.
- Preserve historical revisions rather than silently overwriting records.

## Roadmap

- [ ] UN-country exchange registry
- [ ] Exchange/operator registry
- [ ] Main-board registry
- [ ] Regulator registry
- [ ] Issuer/security identifier schema
- [ ] World Bank WDI stock-market ingestion
- [ ] WFE aggregate ingestion where licensed
- [ ] IMF MFS financial-market ingestion
- [ ] National exchange/regulator adapters
- [ ] Corporate-action normalization
- [ ] Market-data license registry
- [ ] Time-series change detector
- [ ] Financial-market data-gap engine
- [ ] Cross-country comparison dashboard
