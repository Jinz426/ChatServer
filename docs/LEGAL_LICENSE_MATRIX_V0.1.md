# ORBIT Legal / License Matrix v0.1

> Planning document, not legal advice. A license requirement depends on the actual business activity, jurisdiction, data, technology and deployment model. Before launch, obtain advice from qualified counsel in each relevant jurisdiction.

## 0. How to read this matrix

There is rarely one universal "ORBIT license". Requirements attach to specific activities.

`Entity → Activity → Data/Asset → Jurisdiction → Regulator → License / Registration / Contract → Ongoing compliance`

The project should distinguish:

- **Corporate registration** — creates the legal business entity.
- **License / permit** — permission to conduct a regulated activity.
- **Registration / notification** — regulatory filing that may apply without being a conventional license.
- **Contract / terms** — permission from a platform, model provider or data owner.
- **IP right** — trademark, patent, copyright or other intellectual-property protection.
- **Standard / certification** — evidence of security, quality or operational controls; not automatically a government license.

---

## 1. Corporate / company layer 🏢

### Activities
- Software development
- AI platform operation
- Consulting / SaaS
- Commercial contracts
- Hiring staff
- Receiving revenue

### Core items to investigate
- Company / juristic-person registration
- Tax registration and accounting obligations
- Business-specific registrations
- Beneficial-owner / corporate filings where applicable
- Employment and social-security registrations where applicable

### Thailand starting point
Thailand's Department of Business Development (DBD) provides digital juristic-person registration services, including establishment, amendments and dissolution. urlDBD Biz Registhttps://edbr.dbd.go.th/

**Status for ORBIT:** Required once a formal Thai business entity is established; exact structure depends on ownership and activity.

---

## 2. Software / open-source layer 💻

### Activities
- Publishing ORBIT source code
- Distributing binaries
- Including third-party dependencies
- Commercial use

### Required legal controls
- Choose an ORBIT project license.
- Maintain `THIRD_PARTY_NOTICES`.
- Record every dependency and its license.
- Preserve required copyright / attribution notices.
- Check source-available restrictions separately from open-source licenses.
- Do not copy Apple, LLVM, Swift, MLX or other upstream source into ORBIT unless the applicable license permits the intended use.

**Status:** License selection required before broad redistribution.

---

## 3. Intellectual-property layer ™️

### Activities
- ORBIT name / logo
- New compiler technology
- New algorithms or technical inventions
- Documentation and source code
- Dataset / schema design

### Items
- Trademark search and registration where commercially useful.
- Copyright notices and ownership records.
- Patentability review before public disclosure of potentially patentable inventions.
- Contributor License Agreement (CLA) or Developer Certificate of Origin if the project adopts one.
- Invention-assignment agreements for employees/contractors where appropriate.

For Thailand, the Department of Intellectual Property (DIP) is the relevant starting authority for national IP matters.

**Status:** Protect the project name and important inventions before commercialization where appropriate.

---

## 4. User-data / privacy layer 🔐

### Activities
- Importing ChatGPT exports
- Reading authorized files
- Photos / metadata
- Notes / calendars
- AI conversation history
- User Knowledge Graph
- Cross-model processing

### Required controls
- Lawful basis / appropriate consent mechanism.
- Clear purpose limitation.
- Data minimization.
- Privacy notice.
- Access / correction / deletion workflows where applicable.
- Retention schedule.
- Revocation workflow.
- Processor / controller role analysis.
- Cross-border transfer assessment.
- Security safeguards.
- Incident / breach response.
- Sensitive-data handling rules.

**Important:** A user authorization to import data is not a blanket authorization to share it with every AI provider.

**Status:** Mandatory compliance work before processing real users' personal data.

---

## 5. AI model / provider layer 🤖

### Activities
- Connecting OpenAI or other APIs
- Local models
- Apple model frameworks
- Model adapters
- Multi-model routing
- Using model outputs commercially

### Required controls
- Provider terms of service.
- API/developer agreement.
- Usage restrictions.
- Input-data rights.
- Output-use restrictions.
- Training / fine-tuning restrictions.
- Attribution requirements.
- Retention settings.
- Rate limits.
- Model-specific safety requirements.
- Cost and billing records.

**Status:** Every provider adapter needs its own compliance record.

---

## 6. Siri / Apple platform layer 🍎

### Activities
- App Intents
- Siri integration
- Apple Intelligence integration
- App Store distribution
- In-app purchases / paid services

### Required controls
- Apple Developer Program agreement.
- App Store Review requirements.
- Privacy disclosures and permissions.
- Required entitlements / capabilities.
- Paid Apps Agreement where applicable.
- Rules applicable to Apple Intelligence / Foundation Models features.

**Status:** Required if the product is distributed through Apple's ecosystem.

---

## 7. Digital-platform layer 🌐

### Activities
- Marketplace
- AI service marketplace
- Connecting users and providers
- Seller / buyer platform
- Ranking / recommendation
- User-generated content

### Required controls
- Platform terms.
- Consumer protection.
- Seller verification where applicable.
- Content moderation / reporting.
- Dispute process.
- Advertising disclosure.
- Applicable digital-platform registration / notification.

### Thailand
Thailand's Electronic Transactions Development Agency (ETDA) administers the Digital Platform Services regulatory framework. Applicability depends on the actual platform activity and thresholds.

**Status:** Assess before operating a marketplace or regulated digital platform in Thailand.

---

## 8. Payment / money layer 💳

### Activities
- Accepting payments for ORBIT services
- Payment processing for third parties
- Wallet / stored value
- Electronic money
- Money transfer
- Settlement between users

### Key distinction
Using a licensed third-party payment processor to collect payment is different from becoming the regulated payment provider yourself.

### Thailand
The Bank of Thailand states that designated payment systems and designated payment services may require a Ministry of Finance license or BOT registration before operation. Covered activities include electronic money, receiving electronic payments on behalf of merchants, electronic money transfer and other regulated payment services. citeturn0search1turn0search5

**Status:** Determine the exact payment flow before implementation. Do not launch a self-operated wallet/payment service without regulatory analysis.

---

## 9. Digital-asset / token layer 🪙

### Activities
- Tradable token
- Exchange
- Brokerage
- Dealer activity
- Custody
- Digital-asset wallet service
- Token fundraising
- Secondary market

### Important ORBIT rule
**OSU is currently only a workload/accounting unit. It is not automatically money, electronic money, a security or a digital asset.**

If ORBIT later creates a transferable token with economic value, obtain jurisdiction-specific legal analysis before launch.

### Thailand
Thailand's SEC provides a licensing framework for digital-asset businesses and publishes application materials for digital-asset business licenses. citeturn0search10turn0search20

**Status:** No tradable financial token should be launched under the assumption that it is unregulated.

---

## 10. AI work / employment / contractor layer 👷

### Activities
- AI-generated work sold to customers
- Human reviewers
- AI agents performing tasks
- Revenue sharing
- Contractor marketplace

### Controls
- Worker classification.
- Employment contracts.
- Contractor agreements.
- IP assignment / licensing.
- Tax withholding where applicable.
- Social-security obligations where applicable.
- Human approval for regulated professional work.

**Status:** Required as soon as human labor and commercial revenue-sharing are introduced.

---

## 11. Product / commerce layer 📦

### Activities
- Product identification
- Product marketplace
- Price comparison
- Import/export
- Product recommendations
- Selling physical goods

### Controls
- Consumer protection.
- Product labeling.
- Product safety.
- Import/export permits.
- Customs.
- VAT / sales taxes as applicable.
- Sector-specific approvals for regulated products.

**Status:** Depends on product category and country.

---

## 12. Food / water layer 💧🌾

### Activities
- Drinking-water production
- Food production
- Agriculture
- Packaging
- Distribution

### Controls
- Food / beverage establishment authorization.
- Product registration or notification where applicable.
- Sanitation and quality standards.
- Packaging / labeling requirements.
- Water-source permissions where applicable.
- Environmental approvals.
- Factory permissions if manufacturing scale triggers them.

**Status:** Separate regulatory track from the software platform.

---

## 13. Factory / industrial layer 🏭

### Activities
- Manufacturing
- Chemical/material processing
- Industrial machinery
- Large-scale production

### Controls
- Factory license / registration where applicable.
- Building and land-use approvals.
- Occupational safety.
- Fire safety.
- Hazardous-material controls.
- Wastewater / emissions controls.
- Environmental impact assessment where required.

**Status:** Country and factory-category specific.

---

## 14. Land / construction / city-planning layer 🏗️🌳

### Activities
- Land development
- Housing
- Factory zones
- Markets
- Roads
- Utility corridors
- Protected land

### Controls
- Land title / ownership verification.
- Zoning / land-use permission.
- Building permits.
- Construction permits.
- Environmental assessment.
- Utility approvals.
- Protected-area restrictions.
- Transport / road approvals.

### Environmental assessment
Thailand's ONEP maintains an environmental assessment information system covering IEE/EIA/EHIA projects. citeturn0search13

**Status:** GIS analysis can begin with public data; actual development requires project-specific approvals.

---

## 15. GIS / map / location-data layer 🗺️

### Activities
- Coordinate analysis
- Road maps
- Property / land-use analysis
- Navigation
- Geospatial datasets
- Commercial mapping

### Controls
- Map-data license.
- Dataset terms.
- Personal-location privacy.
- Restrictions on sensitive locations where applicable.
- Survey / cadastral-data rights.
- Provider API limits.

**Status:** Each map/data provider needs a source-license record.

---

## 16. Financial markets / investment layer 📈

### Activities
- Investment advice
- Brokerage
- Securities marketplace
- Fund management
- Equity issuance
- Crowdfunding

### Controls
- Securities-law analysis.
- Broker/dealer licensing where applicable.
- Investment-adviser licensing where applicable.
- Prospectus / offering rules.
- AML/KYC.
- Market-conduct controls.

**Status:** ORBIT must not present itself as a financial intermediary without jurisdiction-specific authorization.

---

## 17. Cybersecurity layer 🛡️

### Activities
- Security monitoring
- AI agents with system access
- Credentials / secrets
- Threat intelligence
- Incident response

### Controls
- Security management system.
- Access-control policy.
- Key management.
- Audit logging.
- Vulnerability management.
- Incident response.
- Secure software supply chain.
- SBOM.
- Backup / disaster recovery.
- Responsible disclosure.

**Status:** Security controls are required even where no special government license applies.

---

## 18. International / cross-border layer 🌍

For every country in which ORBIT operates, create a jurisdiction record:

```text
Country
Legal entity
Tax
Privacy
AI
Data transfer
Payment
Digital assets
Consumer protection
IP
Employment
Map/GIS
Product regulation
Environmental regulation
Local representative requirement
Regulator contacts
License status
Expiry / renewal
```

Never assume that a license in one country automatically authorizes activity in another.

---

# ORBIT Compliance Status Model

Every capability should have one of these statuses:

`NOT_REVIEWED`
`NOT_APPLICABLE`
`CONTRACT_REQUIRED`
`REGISTRATION_REQUIRED`
`LICENSE_REQUIRED`
`APPROVED`
`EXPIRED`
`SUSPENDED`
`PROHIBITED`

Each record should also contain:

```text
jurisdiction
regulator
legal_basis
activity
license_type
application_url
owner
issue_date
expiry_date
conditions
last_reviewed
next_review
legal_counsel
```

# Recommended implementation order

1. Corporate entity + tax
2. IP ownership + project license
3. Privacy / user-data governance
4. AI-provider contracts
5. Apple / platform agreements
6. Cybersecurity controls
7. Payment model review
8. Digital-platform review
9. Digital-asset review if OSU ever becomes transferable
10. Country-by-country regulatory matrix
11. Physical-product / factory / food / land permits only when those business lines are actually launched

# Principle

**Do not obtain licenses simply because the architecture mentions a capability. Obtain the authorization required by the activity actually performed.**

The ORBIT architecture should therefore be designed so regulated capabilities can be disabled until the relevant legal, contractual and technical requirements are satisfied.
