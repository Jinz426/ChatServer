# Country License Registry Schema v0.1

## Purpose

Extend the UN 193 Member State registry with a structured, jurisdiction-aware catalog of permits, licenses, registrations, approvals and regulatory obligations.

The registry is a **research and planning layer**, not legal advice. A country entry must distinguish verified official requirements from hypotheses or items requiring local counsel confirmation.

## Country record

Each UN member state should eventually contain:

```text
country
  un_member_state
  iso_3166_1_alpha2
  iso_3166_1_alpha3
  iso_3166_numeric
  official_name
  jurisdictions
  regulators
  licensing_portal
  tax_authorities
  data_protection_authority
  intellectual_property_authority
  last_verified
  source_registry
```

## License record

```text
license
  id
  country
  jurisdiction_level
  regulator
  activity
  sector
  instrument_type
  official_name
  application_url
  legal_basis
  prerequisites
  required_documents
  fees
  validity_period
  renewal
  reporting
  inspection
  penalties
  foreign_ownership_rules
  cross_border_rules
  data_requirements
  status
  effective_from
  effective_to
  source_url
  verification_date
  confidence
```

## Jurisdiction levels

Each country can be modeled as:

```text
UN member state
  ↓
National / Federal
  ↓
State / Province / Region
  ↓
District / County
  ↓
Municipality / City
  ↓
Special economic / industrial / free-trade zone
```

Not every country uses all levels. The registry must represent the actual constitutional and administrative structure of each jurisdiction.

## Cross-country activity taxonomy

Start with a common taxonomy, then map local legal names to it:

1. Business formation
2. Tax registration
3. Employment / labor
4. Land acquisition / lease
5. Zoning / planning
6. Construction
7. Utilities
8. Factory / industrial operation
9. Environmental approval
10. Water extraction / treatment / sale
11. Food / beverage
12. Agriculture / livestock
13. Mining / natural resources
14. Energy / electricity
15. Chemicals / hazardous materials
16. Transport / logistics
17. Road / rail / aviation / maritime
18. Retail / wholesale / markets
19. Import / export / customs
20. Telecommunications
21. Software / cloud / data processing
22. AI / automated decision systems where regulated
23. Privacy / personal data
24. Cybersecurity where regulated
25. Intellectual property
26. Financial services
27. Payment services
28. Digital assets
29. Insurance
30. Securities / investment
31. Healthcare
32. Pharmaceuticals / medical devices
33. Education
34. Tourism / hospitality
35. Waste management / recycling
36. Broadcasting / media
37. Public procurement
38. Professional services
39. Consumer protection
40. Product safety / certification

## Verification states

Use explicit evidence states:

- `VERIFIED_OFFICIAL`
- `VERIFIED_SECONDARY`
- `REQUIRES_LOCAL_CONFIRMATION`
- `HISTORICAL`
- `UNKNOWN`

Never infer that a permit exists merely because an activity is regulated in another country.

## Data provenance

Every license record must point to an official source where possible. International datasets can provide comparative context, but they do not replace national law or regulator guidance.

The World Bank's Business Ready program provides cross-economy data covering areas such as Business Entry, Business Location, Financial Services, International Trade, Labor, Taxation and Utility Services. These indicators can help prioritize research but are not a substitute for the actual license register. 

## Implementation plan

```text
UN 193 registry
      ↓
ISO identifiers
      ↓
Country profile
      ↓
Administrative jurisdictions
      ↓
Regulator directory
      ↓
Activity taxonomy
      ↓
Official permit/license sources
      ↓
Normalized license records
      ↓
Verification + timestamp
      ↓
ORBIT regulatory graph
```

## Important distinction

A regulatory requirement may be:

- a license
- a permit
- a registration
- a notification
- an accreditation
- a certification
- an approval
- a concession
- a tax obligation
- a contractual requirement
- or no special authorization at all.

The registry therefore uses the broader term **Regulatory Instrument** instead of assuming everything is a license.

## Goal

Eventually every one of the 193 UN Member States can have the same machine-readable structure while retaining its own legal reality. The result should allow an authorized user to ask:

> "I want to perform activity X at coordinate Y. What legal and regulatory steps apply here?"

The system should return the jurisdiction, relevant regulatory instruments, official authorities, official sources, verification date, and uncertainty—rather than pretending to make a legal determination.
