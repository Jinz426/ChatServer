# Internet Naming & Official Website Source Registry v0.1

## Purpose
Add IANA and ICANN as foundational Internet naming and identifier sources for the global official-source registry. This layer complements the UN country registry, ISO registry, government-source registry, financial-market registry, WIPO, IMF and World Bank layers.

## Authority model

### IANA
IANA functions coordinate globally unique Internet identifiers, including DNS root-zone delegations, IP address and AS number coordination, protocol registries, the .INT and .ARPA registries, IDN practices and DNSSEC root-key information.

Primary sources:
- https://www.iana.org/
- https://www.iana.org/domains/root/db
- https://www.iana.org/domains/root
- https://www.iana.org/protocols
- https://www.iana.org/numbers
- https://www.iana.org/time-zones

### ICANN
ICANN is the policy and coordination organization associated with the global DNS namespace and the IANA functions. The registry must keep ICANN governance/policy information separate from IANA operational registries.

Primary source:
- https://www.icann.org/

## Website-source registry
Each official website/source record should contain:
- source_id
- country_code
- organization
- organization_type
- jurisdiction
- official_domain
- official_url
- registry_url
- dataset_url
- api_url
- rdap_url
- whois_url
- source_category
- authority_level
- language
- access_method
- authentication_required
- license_status
- terms_url
- robots_status
- last_verified
- last_updated
- historical_urls
- source_status

## DNS / domain registry entities
Track:
- TLD
- TLD type: ccTLD / gTLD / sponsored / IDN
- TLD manager
- registry operator
- delegation status
- DNSSEC status
- RDAP endpoint
- WHOIS endpoint where applicable
- registration-service URL
- delegation update timestamp
- IANA source record

The IANA Root Zone Database is the authoritative source for TLD delegation details and identifies TLD managers. The root zone includes both country-code and generic TLDs.

## Country website discovery model
For each UN member country, discover and verify:
1. National government portal
2. Parliament / legislature
3. Presidency / head-of-government portal where applicable
4. National statistics office
5. Ministry of Finance
6. Central bank / monetary authority
7. Securities regulator
8. Stock exchange
9. Banking regulator
10. Tax authority
11. Company registry
12. Land / cadastral authority
13. GIS / mapping authority
14. Customs / trade authority
15. Agriculture authority
16. Industry authority
17. Transport authority
18. Environment authority
19. Patent / trademark office
20. Official open-data portal
21. National domain registry / ccTLD manager

## Source verification
The system must distinguish:
- PRIMARY_OFFICIAL
- OFFICIAL_REGULATOR
- OFFICIAL_MARKET_OPERATOR
- OFFICIAL_STATISTICS
- INTERNATIONAL_ORGANIZATION
- LICENSED_PROVIDER
- SECONDARY_SOURCE
- UNVERIFIED

A domain matching a country-code TLD is not sufficient evidence that a website is a government source. Organization identity, official references, registry information and source provenance must be verified.

## Global website knowledge graph

UN Country
→ ISO code
→ country-code TLD
→ national domain registry
→ government portal
→ ministries/agencies
→ regulators
→ financial institutions
→ exchanges
→ companies
→ datasets/APIs
→ legal and licensing sources

## Data-gap states
COMPLETE
PARTIAL
STALE
CONFLICTING
NOT_PUBLIC
LICENSE_RESTRICTED
OFFLINE
NOT_VERIFIED
NOT_APPLICABLE

## Update policy
Version every source record. Preserve historical domains and organizational changes. Do not delete historical source identities merely because an organization changes its name, domain or mandate.

## License and redistribution
The registry stores links and metadata about external sources. It does not automatically copy or redistribute third-party datasets. Each source retains its own terms, licenses, access restrictions and attribution requirements.
