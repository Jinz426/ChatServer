# Global Payment Rails Registry v0.1

## Purpose
Create a vendor-neutral registry of payment channels and financial-market infrastructures operating globally, connecting banks, merchants, consumers, governments and cross-border payment systems.

This is an interoperability and knowledge registry. It does not grant access to payment networks or financial accounts.

## 1. Payment-rail taxonomy

### A. Central-bank / wholesale settlement
- RTGS systems
- central-bank settlement accounts
- large-value payment systems
- correspondent-banking settlement
- securities-linked settlement where relevant

### B. Retail clearing
- ACH systems
- direct-debit systems
- domestic credit-transfer systems
- cheque clearing where still active
- bill-payment systems

### C. Instant / fast payments
- domestic instant-payment systems
- account-to-account instant payments
- proxy/address-based payments
- QR payment rails
- request-to-pay systems
- interoperable instant-payment schemes

### D. Card networks
- global card schemes
- domestic card schemes
- debit/credit/prepaid networks
- ATM networks
- merchant-acquiring networks
- card clearing and settlement

### E. Mobile-money and wallet systems
- mobile-money schemes
- e-wallets
- stored-value systems
- telecom-linked payments
- agent networks

### F. Cross-border payment infrastructure
- correspondent banking
- cross-border ACH
- payment-system linkages
- regional payment systems
- instant-payment interconnections
- remittance networks
- foreign-exchange settlement infrastructure

### G. Messaging / interoperability
- financial messaging networks
- ISO 20022 ecosystems
- payment identifiers
- routing/addressing schemes
- API/open-banking interfaces

### H. Digital-asset payment infrastructure
- regulated payment-token systems where applicable
- stablecoin payment rails where legally permitted
- blockchain settlement networks
- regulated crypto payment providers

Digital-asset rails remain a separate layer from sovereign-money payment systems.

## 2. Registry schema

```text
payment_rail_id
rail_name
country_iso_3166_1
jurisdiction
region
operator
operator_type
regulator
legal_status
rail_type
settlement_type
currency
settlement_currency
message_standard
identifier_scheme
participants
banks_supported
non_bank_participants
merchant_access
consumer_access
cross_border
interoperability_links
operating_hours
settlement_finality
pricing_model
official_website
official_rules_url
technical_documentation_url
api_url
source_url
source_license
observed_at
last_verified
status
```

## 3. Examples of system categories
BIS payment-system statistics distinguish large-value, retail and fast payment systems. Its published tables include systems such as Australia's NPP/RITS, Brazil's SPI/STR, India's UPI/RTGS/NEFT, Japan's Zengin/BOJ-NET, Singapore's FAST/MEPS+, the UK's Faster Payments/CHAPS/BACS, and the US FedNow/Fedwire/CHIPS/FedACH. The registry should ingest such information from authoritative national operators and regulators rather than treating the international statistics as a substitute for primary records.

## 4. International standards and infrastructure
Connect the registry to:
- BIS / CPMI payment-system statistics and standards
- World Bank payment-system programmes
- ISO 20022
- SWIFT messaging ecosystem
- national central banks
- national payment-system operators
- regional payment systems
- card-network operators
- regulated payment institutions

## 5. Cross-border connectivity graph

```text
Country A
  ↓
Domestic Bank
  ↓
Domestic Payment Rail
  ↓
Cross-Border Connector / Correspondent / Scheme
  ↓
Foreign Payment Rail
  ↓
Foreign Bank / Wallet
  ↓
Recipient
```

For each connection record:
- participating jurisdictions
- currencies
- settlement mechanism
- message layer
- FX mechanism
- operating rules
- fees where officially published
- settlement time
- access requirements
- regulatory basis
- source/provenance

## 6. Payment-instrument layer
Track, where officially available:
- cash
- cards
- account transfers
- direct debits
- mobile money
- e-money
- QR payments
- instant payments
- cheques
- remittances
- government payments
- merchant payments

BIS payment statistics provide indicators for payment cards, terminals, cashless payment volumes and values, fast payments, payment accounts and payment-service providers.

## 7. Global interoperability layer
Record whether a rail is:
- domestic only
- regionally interoperable
- bilaterally connected
- multilateral
- globally accessible through intermediaries
- planned / pilot
- discontinued

BIS Project Nexus is an example of an architecture intended to connect domestic instant-payment systems through a standardized connection model. It should be represented as an interoperability initiative rather than as a universal global payment network.

## 8. Financial institution relationship

```text
Country
 ↓
Central Bank / Regulator
 ↓
Payment System Operator
 ↓
Payment Rail
 ↓
Participant Banks / PSPs
 ↓
Acquirer / Wallet / Merchant
 ↓
End User
```

Connect each payment rail to the Global Bank Registry, currency registry, company registry and financial-market infrastructure registry.

## 9. Data quality and provenance
Every rail must have:
- authoritative source
- operator source
- regulatory source
- publication date
- effective date
- retrieval timestamp
- version
- methodology
- license/access conditions
- verification status

Statuses:
`VERIFIED_OFFICIAL`, `OFFICIAL_PARTIAL`, `INTERNATIONAL_STATISTICS`, `LICENSE_RESTRICTED`, `STALE`, `CONFLICTING`, `DISCONTINUED`, `UNKNOWN`.

## 10. Privacy and security
The registry stores system-level metadata, not payment credentials, account balances, private transaction histories, authentication secrets or personal financial records.

No connector should bypass authentication, transaction controls, regulatory restrictions or payment-network security.

## 11. Planned ingestion coverage
- All UN-member-country national payment-system sources
- Central banks
- Payment-system operators
- Banking regulators
- Domestic card schemes
- International card schemes
- Mobile-money systems
- Major regulated wallets/payment institutions
- Regional payment systems
- Cross-border payment linkages
- BIS/CPMI datasets
- World Bank payment-system resources

## 12. Completion rule
A payment channel is considered complete only when its operator, legal/regulatory status, participants, rail type, settlement model, source provenance, versioning and access/licensing conditions are documented and validated.
