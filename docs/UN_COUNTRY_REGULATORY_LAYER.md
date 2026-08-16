# UN Country Regulatory Layer v0.1

## Purpose

Use the United Nations Member State list as the top-level country/jurisdiction index for ORBIT's global regulatory, economic, geographic and development datasets.

The UN currently has **193 Member States**. The authoritative membership list is maintained by the United Nations.

Source: https://www.un.org/en/about-us/member-states

## Data model

Each country record should eventually connect to:

```text
UN Member State
   ↓
Country / jurisdiction identifiers
   ↓
Administrative divisions
   ↓
Coordinates / GIS
   ↓
Land use
   ↓
Population
   ↓
Housing / commerce / industry
   ↓
Infrastructure / transport
   ↓
Agriculture / resources
   ↓
Prices / wages / currencies
   ↓
Trade / supply chains
   ↓
Environmental indicators
   ↓
Laws / regulators / licenses
   ↓
AI / digital-policy rules
```

## Important distinction

The **193 UN Member States** are one dataset. Permanent observers, territories, dependencies, disputed areas and other geographic entities must be represented in separate datasets with explicit status fields. They should not be silently mixed into the Member State count.

## Planned country schema

```json
{
  "un_member_state": true,
  "un_name": "Example",
  "iso_alpha2": null,
  "iso_alpha3": null,
  "iso_numeric": null,
  "admission_date": null,
  "official_name": null,
  "capital": null,
  "currency": [],
  "languages": [],
  "regulators": [],
  "licenses": [],
  "privacy_law": [],
  "ai_law": [],
  "digital_platform_rules": [],
  "payment_rules": [],
  "digital_asset_rules": [],
  "land_rules": [],
  "environmental_rules": [],
  "industrial_rules": [],
  "food_water_rules": [],
  "transport_rules": [],
  "trade_rules": [],
  "data_sources": []
}
```

## Why this matters

This creates a common country dimension for the rest of the project. The same country key can be joined to price observations, products, factories, markets, roads, land-use data and regulatory requirements.

It also lets ORBIT compare countries without assuming that political boundaries, economic zones, regulatory jurisdictions and physical geography are identical concepts.

## Update policy

- Keep the UN source URL and retrieval date.
- Do not silently change membership status.
- Version every dataset update.
- Preserve historical membership changes when building time-series data.
- Cross-check country names and codes with authoritative standards before production use.

## Next datasets

1. UN Member States + ISO identifiers
2. UN regional groupings
3. UN agencies and country programmes
4. Country administrative divisions
5. Country regulators
6. License catalogue
7. Economic indicators
8. Land and infrastructure indicators
9. Global product and price observations
10. Country-to-country supply-chain relationships
