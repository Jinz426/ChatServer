# Global Top 100,000 Enterprise Registry v0.1

## Objective
Add a global corporate-entity layer covering up to 100,000 significant enterprises, using multiple ranking and official-source systems rather than pretending that one published ranking contains all 100,000 companies.

## Important methodology
There is no single authoritative public "top 100,000 companies" list. Different rankings measure different things. Therefore this registry must preserve the ranking source and metric instead of creating a false universal rank.

Initial reference families:
- Fortune Global 500 — primarily revenue-based
- Forbes Global 2000 — public companies ranked using sales, profits, assets and market value
- National stock-exchange and regulator lists
- National business/company registries where public
- Industry-specific rankings
- Official issuer filings and annual reports
- LEI / legal-entity datasets where lawfully accessible
- World Bank / IMF / national statistical business indicators

The 2026 Forbes Global 2000 uses four equally weighted dimensions: sales, profits, assets and market value. The 2026 Fortune Global 500 ranks the largest corporations by revenue. These must remain separate source rankings.

## Canonical enterprise entity
Each company receives a stable internal identifier:
`enterprise_id`

Core fields:
- enterprise_id
- legal_name
- trading_name
- aliases
- parent_entity_id
- ultimate_parent_entity_id
- subsidiary_relationship
- jurisdiction
- incorporation country
- headquarters country/city
- official domain
- official investor-relations page
- company registry identifier
- LEI where available
- ticker(s)
- ISIN(s) where available
- exchange/MIC
- sector
- industry
- products/services
- employees
- revenue
- profit
- assets
- liabilities
- equity
- market value
- fiscal year
- reporting currency
- ownership type
- public/private/state-owned/cooperative/nonprofit classification
- founding date
- current status
- source
- source date
- data version
- license/access status

## Ranking model
Never store only `global_rank`.

Use:
- ranking_source
- ranking_year
- ranking_metric
- ranking_scope
- ranking_rank
- methodology_version
- reference_period

Examples:
`FORTUNE_GLOBAL_500 / 2026 / REVENUE / GLOBAL / 1`
`FORBES_GLOBAL_2000 / 2026 / COMPOSITE / GLOBAL / 1`

## Corporate hierarchy

```text
Ultimate Parent
   |
   +-- Subsidiary
   |      +-- Subsidiary
   |      +-- Joint Venture
   |
   +-- Brand
   |
   +-- Listed Issuer
   |
   +-- Operating Company
   |
   +-- Foundation / Nonprofit entity
```

Ownership relationships must be time-versioned because control and ownership change.

## Enterprise categories
The registry should cover:
- banking and financial services
- insurance
- energy
- mining and materials
- manufacturing
- electronics
- semiconductors
- telecommunications
- internet/platforms
- software
- AI
- cloud/data centers
- automotive
- aerospace
- defense where lawful public corporate data is appropriate
- pharmaceuticals
- biotechnology
- healthcare
- agriculture
- food and beverages
- retail
- wholesale
- logistics
- shipping
- airlines
- rail
- construction
- engineering
- chemicals
- utilities
- real estate
- media
- entertainment
- professional services
- consumer goods
- industrial equipment
- environmental/recycling
- education
- hospitality
- other nationally material sectors

## Cross-linking
Every enterprise should be connectable to:
- country/jurisdiction
- government regulator
- tax/customs system where public
- bank/payment relationships where public and lawful
- stock exchange and security identifiers
- patents/trademarks through WIPO/national offices
- factories and facilities where publicly documented
- products and brands
- suppliers/customers where publicly documented
- materials and elements
- energy/resource consumption where disclosed
- workforce indicators
- environmental disclosures
- transport/logistics infrastructure
- internet/network infrastructure
- financial statements
- corporate actions
- mergers/acquisitions
- insolvency/dissolution history

## Entity resolution
Use multiple identifiers and evidence before merging records:
- legal name normalization
- registration number
- LEI
- ISIN/ticker relationship
- official domain
- headquarters
- parent/subsidiary relationship
- regulator/exchange record
- annual report

Never merge two companies solely because their brand names are similar.

## Private-company coverage
The 100,000 target should not be limited to listed companies. Where lawful public data exists, include significant private enterprises, state-owned enterprises and cooperatives. Clearly mark missing financial metrics rather than estimating them as facts.

## Historical layer
Maintain:
- name changes
- mergers
- acquisitions
- spin-offs
- ownership changes
- listings/delistings
- bankruptcies
- restructuring
- jurisdiction changes
- fiscal-year changes
- discontinued operations

## Data-quality statuses
- VERIFIED_OFFICIAL
- VERIFIED_REGULATOR
- VERIFIED_EXCHANGE
- VERIFIED_ISSUER
- VERIFIED_RANKING_SOURCE
- SECONDARY_SOURCE
- ESTIMATED
- HISTORICAL
- DISCONTINUED
- CONFLICTING
- UNVERIFIED

## Privacy and access
Do not ingest private personal information about employees, directors, customers or shareholders unless there is a lawful and necessary public-data basis. Executive contact lists and personal identifiers are not required for the core enterprise graph.

## Data licensing
Ranking datasets may have proprietary terms. The registry should store references, identifiers, methodology and links where permitted, and ingest licensed datasets only under their applicable terms. Do not copy proprietary ranking databases wholesale without permission.

## Target architecture

```text
100,000 Enterprise Entities
          |
          +-- Country
          +-- Sector
          +-- Industry
          +-- Ownership
          +-- Parent/Subsidiary
          +-- Exchange/Security
          +-- Products/Brands
          +-- Facilities
          +-- Supply Chain
          +-- Materials
          +-- Finance
          +-- Payments
          +-- Patents/IP
          +-- Workforce
          +-- Environment
          +-- Internet/Infrastructure
          |
          v
    GLOBAL KNOWLEDGE GRAPH
          |
          v
        ORBIT
```

## Implementation phases
### Phase 1
- canonical enterprise schema
- ranking-source schema
- country/sector taxonomy
- entity-resolution rules
- source/provenance registry

### Phase 2
- Fortune/Forbes reference ingestion
- exchange/regulator issuer ingestion
- LEI and official registry crosswalks
- national company-source adapters

### Phase 3
- corporate hierarchy graph
- historical events
- financial time series
- supply-chain/product/facility links

### Phase 4
- scale toward 100,000 entities
- automated source refresh
- conflict/data-gap engine
- global enterprise dashboard

## Completion rule
"Top 100,000" is a project coverage target, not a claim that one ranking defines the world's 100,000 largest enterprises. Each enterprise and each ranking must retain its source, metric, period, methodology, provenance and license status.
