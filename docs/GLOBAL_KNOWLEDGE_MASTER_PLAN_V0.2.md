# Global Knowledge Master Plan v0.2

## Purpose
This master plan consolidates the project from the beginning into one canonical architecture. It is a roadmap and registry specification; a listed component is NOT considered implemented merely because its schema or documentation exists.

## Ground truth
The UN currently has 193 Member States. The project uses that as the country backbone, while separately representing observer states, territories, jurisdictions and disputed/administrative areas. Official UN sources should be used for membership metadata.

## Core architecture

```text
                         WORLD
                           |
                 CANONICAL ENTITY ID
                           |
      +--------------------+--------------------+
      |                    |                    |
   PLACE              ORGANIZATION           OBJECT
      |                    |                    |
 Country/Land        Gov/Bank/Company     Product/Material
 Building/Road       Regulator/Exchange   Component/Device
      |                    |                    |
      +--------------------+--------------------+
                           |
                    DATASET / EVENT
                           |
                     PROVENANCE
                           |
                 EVIDENCE / INFERENCE
                           |
                         ORBIT
                           |
                 AI / EMBED / APIS
```

## A. Global identity, standards and source registry
- UN 193 Member States
- observer states and other jurisdiction classes
- ISO 3166 country/subdivision
- ISO 4217 currencies
- ISO 639 languages
- ISO 8601 dates/time
- IANA registries
- ICANN ecosystem
- ITU standards/statistics
- WIPO patents/trademarks/IP metadata
- IEEE standards and technology metadata
- official government source registry
- official API/dataset registry

Required source fields: jurisdiction, organization, official domain, endpoint, dataset, source type, legal authority, license, access method, language, update frequency, last verified, status.

## B. Geography and physical world
- coordinates and administrative boundaries
- land use/zoning/cadastre where public
- residential areas and buildings
- commercial districts, shops and markets
- factories and industrial zones
- farms and agricultural land
- roads, rail, metro, bus, freight, pedestrian and bicycle networks
- ports, airports and logistics nodes
- population and settlement change
- climate, environment and disaster constraints
- satellite/remote-sensing observations where licensed

## C. Elements, materials and manufacturing
- periodic-table element registry
- isotopes
- minerals and geological resources
- compounds
- alloys
- semiconductors
- batteries and energy materials
- ceramics, polymers and composites
- electronic components
- manufacturing processes as metadata
- mining/refining/manufacturing provenance
- recycling and material recovery

Relationship: `Element -> Resource -> Material -> Component -> Product -> Recovery`.

## D. Electronics and EMBED
Global electronics registry covering consumer, computing, networking, telecom, displays, imaging, audio, wearables, IoT, industrial, automotive, robotics, semiconductor, storage, sensors, test equipment and other electronic products.

Entity chain:
`Brand -> Legal Entity -> Parent -> OEM/ODM -> Product Family -> Model/SKU -> Hardware Revision -> Firmware -> API/Standards -> Lifecycle`.

EMBED language:
- declarative device description
- capability discovery
- permission scopes
- vendor-neutral adapters
- explicit consent for privileged actions
- hardware capability probe
- auditability

## E. Biological and life sciences
- blood-group and transfusion systems
- national blood services and public inventory statistics
- biobank institution/catalog metadata
- genomics/genome assemblies
- genes, variants, transcripts
- CRISPR/genome-editing scientific metadata
- proteins, peptides and structures
- pathways and interactions
- cell types, cell lines and organoids
- microbiology
- immunology
- synthetic biology metadata
- bioinformatics resources
- agriculture/plant genomics
- veterinary genetics
- biodiversity/species/taxonomy
- scientific publications and patents

Public/authorized sources may include NCBI, GenBank, EMBL-EBI/ENA, DDBJ, UniProt, RCSB PDB, InterPro, Ensembl, GBIF, Catalogue of Life, IUCN, WIPO and national repositories, subject to terms.

Human genomic, donor, patient and biobank data must use appropriate access controls; the public graph stores references and metadata rather than private identities.

## F. Financial institutions
For every jurisdiction, build a source-backed registry for:
- central bank
- banking regulator
- commercial banks
- state-owned banks
- development banks
- foreign bank branches/subsidiaries
- Islamic banks
- cooperative/credit institutions
- microfinance/specialized institutions
- digital banks/neobanks where legally recognized
- license/status history
- branches/ATMs where public
- SWIFT/BIC, LEI and national identifiers where available

Bank status must be verified against the competent regulator; international statistics are supplementary rather than a substitute for licensing records.

## G. Financial system and currencies
- sovereign/national currency registry
- ISO 4217
- exchange-rate history
- central-bank balance sheets and policy rates
- deposits/credit/financial inclusion
- World Bank WDI/GFDD/Global Findex
- IMF Financial Access Survey and relevant IMF datasets
- BIS banking/credit/exchange/payment statistics
- financial-system comparison
- data-gap and change detection

## H. Capital markets
- securities regulators
- exchanges/operators
- main boards and market segments
- issuers
- securities identifiers (ISIN/LEI/MIC and local identifiers)
- official filings
- corporate actions
- clearing houses/CCPs
- central securities depositories/CSDs
- trade repositories
- market-data licensing
- WFE aggregates where licensed
- cross-country comparison

## I. Payment rails
Separate payment rails from instruments, institutions and currencies.

Registry classes:
- RTGS / large-value systems
- ACH / retail clearing
- fast/instant payment systems
- card networks/schemes
- ATM networks
- mobile money
- e-wallets
- QR systems
- correspondent banking
- cross-border connectors
- FX settlement/PvP infrastructure
- financial messaging
- ISO 20022
- regional payment systems
- digital-asset rails where lawful

BIS/CPMI Red Book data is a major reference for payment systems, FMIs and critical providers; it distinguishes large-value, retail and fast payment systems and also covers CSD/CCP/trade-repository infrastructure.

## J. Internet and telecom
- IANA
- ICANN
- AFRINIC/APNIC/ARIN/LACNIC/RIPE NCC
- ITU
- national telecom regulators
- operators
- fixed broadband
- mobile networks
- spectrum
- numbering
- submarine cables
- terrestrial fiber
- satellite connectivity
- IXPs
- network quality, coverage and affordability
- digital divide

## K. Product, price and supply chain intelligence
- product ontology
- image observation
- product recognition
- price observations
- unit/pack-size normalization
- quality/grade metadata
- retailer/market observations
- raw-material provenance
- supply-chain graph
- production-cost research
- logistics
- waste/recycling
- circular economy

Observation from an image must remain distinct from inference. A visual estimate of a product price is an observation candidate, not automatically a verified market price.

## L. World Knowledge / evidence engine
- observation schema
- product/price schema
- GIS layer
- historical timeline
- knowledge graph
- source graph
- evidence graph
- data-gap engine
- conflict detection
- confidence/uncertainty
- temporal versioning
- entity resolution
- deduplication
- multilingual labels

Rules:
`OBSERVATION != INFERENCE`
`SOURCE != CLAIM`
`SPECIFICATION != IMPLEMENTATION`
`ESTIMATE != VERIFIED VALUE`

## M. ORBIT runtime
Phase 1: language specification.
Phase 2: lexer, parser, AST, type/unit checker, evidence checker, ORBIT-IR.
Phase 3: runtime, provider adapters, hardware capability probe, work/token meter, ledger.
Phase 4: world-intelligence pipelines, knowledge graph, GIS, product recognition and supply chain.
Phase 5: model orchestration, authorized user ecosystem and public APIs.

## N. Multi-model bridge
- provider-neutral model interface
- model capability registry
- format/language adapters
- routing/orchestration
- context normalization
- provenance
- compute/work metering
- model cost accounting
- explicit permissions

No unrestricted cross-model or cross-account access is assumed.

## O. User-authorized ecosystem
- ChatGPT export ingestion
- other AI export adapters
- local knowledge index
- Apple/Siri App Intents prototype
- consent dashboard
- permission scopes
- revocation
- deletion verification
- export/audit history

## P. Intel / hardware optimization
- CPU/GPU/NPU capability probe
- Intel feature detection
- memory/storage/network benchmark
- compiler/runtime optimization
- quantization experiments
- model acceleration
- reproducible benchmark suite

Performance claims must be measured on actual hardware; software cannot simply turn one CPU into a different physical processor.

## Q. Global Foundation / economic balance
Separate:
- physical assets
- productive capacity
- financial claims
- liabilities
- cash flow
- digital assets
- resources

Never treat market capitalization or token market value as equivalent to physical wealth. Consolidation must prevent double counting.

## R. Governance, legal and safety
- authentication
- authorization / least privilege
- encryption
- secrets management
- audit logs
- data retention/deletion
- jurisdiction/privacy mapping
- third-party license registry
- source terms and API policies
- rate limits
- human review for high-impact data
- biosafety and controlled biological-data boundaries
- reproducible versioned releases

## S. Operations
- scheduled ingestion
- incremental updates
- source health checks
- validation tests
- schema migration
- immutable snapshots
- rollback
- CI/CD
- backup/recovery
- observability
- alerting

## T. Interfaces
- country dashboard
- bank/financial dashboard
- exchange dashboard
- payment-rail map
- telecom coverage map
- physical-world GIS
- materials/elements explorer
- electronics explorer
- biology/science explorer
- supply-chain graph
- product/price explorer
- evidence/provenance viewer
- data-gap dashboard
- consent dashboard
- machine-readable APIs

## U. Priority missing foundations
1. Canonical global entity-ID system
2. Shared ontology and controlled vocabularies
3. Entity resolution/deduplication
4. Temporal history model
5. Unit/currency/time normalization
6. Provenance/data-lineage graph
7. Data-quality/conflict engine
8. Source-adapter framework
9. Licensing/policy engine
10. Privacy/security/consent framework
11. Human review workflow
12. Test/benchmark fixtures
13. Disaster recovery
14. Multilingual/accessibility layer
15. Public machine-readable schemas

## V. Implementation order
1. Canonical IDs + ontology
2. Source registry + provenance
3. Country/jurisdiction registry
4. Time/unit/currency normalization
5. Financial/bank/payment ingestion
6. Internet/telecom ingestion
7. Materials/electronics ingestion
8. Biology/science ingestion
9. GIS/physical-world ingestion
10. ORBIT parser/runtime
11. EMBED device layer
12. Evidence/conflict/data-gap engine
13. Multi-model/user-authorized adapters
14. Dashboards/API
15. Security/legal/operational audit

## Completion standard
A component is COMPLETE only when implementation, tests, source validation, licensing review, provenance, versioning, monitoring and documentation are present. A registry specification or README alone is not completion.

## Current project status
This master plan consolidates the architecture. Individual registry documents may be SPEC, PROTOTYPE, INGESTION, VERIFY or PLANNED. Future work should update status explicitly rather than implying that all world data has already been collected.
