# World Bank Financial System Layer v0.1

## Purpose

Add World Bank financial-system and financial-inclusion data to the ORBIT country model. This layer is for comparative analysis and planning support; it is not a substitute for a country's central bank, financial regulator, legal code, or licensed professional advice.

## Primary World Bank sources

### Global Financial Development Database (GFDD)

The World Bank's Global Financial Development Database describes financial-system characteristics across economies using a 4x2 framework:

- **Depth** — size and activity of financial institutions and markets
- **Access** — ability of people and firms to use financial services
- **Efficiency** — how effectively institutions and markets intermediate resources and facilitate transactions
- **Stability** — resilience/stability of financial institutions and markets

The framework covers both **financial institutions** and **financial markets**, with indicators such as banking, insurance, stock and bond markets. The World Bank currently describes the database as covering 203 economies, with annual historical data and a latest release updated in September 2022 through 2021. Because this dataset is not real-time, ORBIT must store its vintage and last-updated date rather than treating it as live data.

### Global Findex 2025

The Global Findex 2025 provides nearly 300 indicators on financial inclusion, including mobile-phone ownership, internet use, digital safety, account ownership, payments, saving, credit and financial resilience. The 2025 edition uses nationally representative surveys of about 148,000 adults in 141 economies conducted during 2024, with results reported by country, region and income group and many indicators disaggregated by gender, income, labor-force participation, age, and rural/urban residence.

### World Development Indicators / DataBank

Use WDI and DataBank series for broader financial-sector and macroeconomic context, including domestic credit and related financial-sector measures. Always retain the original series code, source, unit, periodicity, reference period and methodology.

## Country financial-system schema

Each country/economy should have a versioned financial profile:

```json
{
  "country_code": "ISO3",
  "economy_name": "Example",
  "reference_date": "YYYY-MM-DD",
  "source_vintage": "World Bank dataset/version",
  "monetary_system": {},
  "financial_institutions": {},
  "financial_markets": {},
  "financial_inclusion": {},
  "credit": {},
  "payments": {},
  "savings": {},
  "insurance": {},
  "pensions": {},
  "digital_finance": {},
  "external_finance": {},
  "financial_stability": {},
  "regulatory_authorities": [],
  "data_quality": {}
}
```

## Financial layers to populate

### 1. Monetary system

Track, from authoritative national/IMF sources where applicable:

- currency and currency code
- monetary authority / central bank
- exchange-rate regime
- policy-rate series
- inflation context
- reserve assets
- monetary aggregates
- payment-settlement infrastructure

World Bank data should be linked where available, but monetary-policy facts should normally be verified against the country's central bank and IMF sources.

### 2. Banking / financial institutions

Track:

- commercial banks
- state-owned banks
- cooperative / credit institutions
- microfinance institutions
- finance and leasing companies
- insurance companies
- pension funds
- other regulated financial corporations
- foreign-bank participation
- concentration / competition indicators
- branches / ATMs and digital access where available

### 3. Financial markets

Track:

- equity markets
- bond markets
- government securities
- corporate debt
- market capitalization
- market turnover / activity
- listed issuers
- institutional investors
- market infrastructure

Market-level legal status must be linked to the appropriate national regulator and exchange rather than inferred from World Bank statistics.

### 4. Financial inclusion

Track:

- account ownership
- mobile-money usage
- payments
- savings
- borrowing
- formal credit
- financial resilience
- digital access
- gender gaps
- income-group gaps
- age groups
- rural / urban gaps

### 5. Credit allocation

Connect:

```text
Households
Businesses / SMEs
Agriculture
Infrastructure
Government
Other sectors
        ↓
Credit providers
        ↓
Credit volume / terms / access
```

Do not infer an individual's creditworthiness from aggregate country indicators.

### 6. Payments and digital finance

Track:

- account-based payments
- card usage
- mobile money
- digital payments
- internet access
- mobile access
- digital safety indicators
- payment-system infrastructure

Payment licensing and e-money rules must come from the relevant national regulator.

### 7. Savings and investment

Track aggregate indicators for:

- formal savings
- informal savings
- deposits
- pension participation
- insurance penetration
- investment-market access

### 8. Financial stability

Track appropriate indicators for:

- bank capital
- asset quality
- liquidity
- profitability
- non-performing loans
- concentration
- systemic risk proxies
- market stability

The system must preserve the methodology and source because stability indicators are not interchangeable across datasets.

## 4x2 comparison matrix

ORBIT should represent the World Bank GFDD framework as:

```text
                         Financial Institutions     Financial Markets
Depth                         ✓                         ✓
Access                        ✓                         ✓
Efficiency                    ✓                         ✓
Stability                     ✓                         ✓
```

This creates a comparable country-level financial-system profile without pretending that one score fully represents an economy.

## Connect finance to the existing ORBIT world model

```text
Land
 ↓
Resources
 ↓
Production
 ↓
Businesses
 ↓
Jobs / Income
 ↓
Banks / Payment Systems
 ↓
Credit / Savings / Investment
 ↓
Consumption
 ↓
Tax / Public Finance
 ↓
Infrastructure
 ↓
Future Production
```

This should connect with the existing:

- country registry
- regulatory/license layer
- population and needs layer
- price/economic layer
- industry/supply-chain layer
- land/resource layer
- infrastructure layer
- circular-economy layer
- AI/value ledger

## Data freshness rules

World Bank financial databases have different vintages and frequencies. ORBIT must never label a historical survey or static database as real-time.

Every financial record should include:

```text
source
source_dataset
indicator_code
reference_period
publication_date
last_verified
vintage
unit
frequency
methodology_version
original_provider
confidence
```

For live or high-frequency financial information, use appropriate current primary sources and regulators in addition to World Bank historical/structural datasets.

## Country regulatory bridge

For each country, financial data should point to the actual authorities responsible for:

- central banking / monetary policy
- banking supervision
- securities markets
- insurance
- pensions
- payment services
- anti-money-laundering controls
- consumer financial protection
- digital assets where applicable

The World Bank dataset describes the financial system; it does **not** itself grant permission to operate a financial business.

## Data quality

World Bank notes that some financial-development datasets may contain errors or omissions and recommends consulting metadata and original data providers. ORBIT should therefore retain source attribution and uncertainty instead of silently filling missing values.

## Roadmap

- [x] World Bank financial-system layer specification
- [ ] Country-level GFDD ingestion
- [ ] Global Findex 2025 ingestion
- [ ] WDI financial-sector indicator ingestion
- [ ] Indicator metadata registry
- [ ] Country financial profiles
- [ ] Central-bank / regulator source registry
- [ ] Financial-system visualization
- [ ] Time-series change detection
- [ ] Financial data-gap engine
- [ ] Cross-country financial-system comparison
