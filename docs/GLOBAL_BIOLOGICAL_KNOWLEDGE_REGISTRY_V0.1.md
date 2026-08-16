# Global Biological Knowledge Registry v0.1

## Scope
Add standards and public-source registries for IEEE technology, blood-bank/transfusion systems, genetic sequence resources, biobanks, species/biodiversity, proteins, structures, pathways and related biological knowledge to the World Knowledge / ORBIT architecture.

## 1. IEEE technology layer
Track, where publicly and lawfully available:
- IEEE standards
- IEEE standards identifiers and versions
- communications/networking standards
- computing and hardware standards
- power/electrical standards
- signal processing
- robotics and automation
- sensors and instrumentation
- semiconductor/electronic engineering references
- published metadata and provenance

Separate standards metadata from copyrighted full-text standards. Record license/access requirements.

## 2. Blood and transfusion knowledge layer
This is an institutional/public-knowledge registry, not a database of private donor identities.

Track:
- blood-group systems
- ABO/Rh and other recognized blood-group antigens
- compatibility rules
- component types
- blood-bank organizations
- national blood services
- transfusion standards/guidelines
- inventory statistics where officially published
- pathogen-screening/public safety standards
- cold-chain and logistics indicators where publicly documented
- country-level blood-supply indicators

Never ingest identifiable donor/patient information into the public knowledge graph.

## 3. Genetic sequence and genomics layer
Track public scientific resources such as:
- nucleotide sequences
- reference genomes
- genome assemblies
- genes and genomic features
- variation resources
- transcript records
- taxonomy links
- accession identifiers
- publication metadata
- provenance and version

Priority public-source integrations may include NCBI/GenBank, EMBL-EBI/ENA and DDBJ, subject to their terms and data policies.

## 4. Biobank layer
Track institutions and public metadata for:
- population biobanks
- disease-oriented biobanks
- tissue repositories
- sample collections
- specimen types
- consent/access policy metadata
- governance
- country/jurisdiction
- data-use requirements
- catalogue/API endpoints where available

Do not store identifiable human biospecimen records or private participant information in the public registry.

## 5. Species and biodiversity layer
Track:
- accepted species names
- synonyms
- taxonomic hierarchy
- taxon identifiers
- geographic distribution where lawfully/publicly available
- conservation status
- habitats
- observations and occurrence metadata
- invasive/threatened status
- protected-species information
- biodiversity datasets
- provenance and observation date

Potential public sources include GBIF, Catalogue of Life, IUCN and national biodiversity authorities, subject to source-specific terms.

## 6. Protein layer
Track:
- protein identifiers
- amino-acid sequences where permitted
- gene relationships
- organism/taxon
- protein function annotations
- domains
- families
- structures
- interactions
- pathways
- evidence level
- database accession and version

Potential public sources include UniProt, RCSB PDB and InterPro/EMBL-EBI, subject to their respective terms.

## 7. Structure and molecular layer
Connect:
`Element -> Molecule -> Gene -> RNA -> Protein -> Complex -> Structure -> Pathway -> Cell/Organism -> Species`

Include identifiers and provenance rather than treating independently sourced records as automatically identical.

## 8. Scientific evidence model
Every biological observation should carry:
- canonical entity ID
- source database
- accession/identifier
- source version
- publication/reference
- observation date
- retrieval date
- evidence type
- confidence/curation status
- license/access status

Separate:
`OBSERVATION != ANNOTATION != INFERENCE`

## 9. Privacy and biosafety
The registry is intended for public scientific knowledge and institutional metadata. It must not expose private patient/donor information or enable unauthorized access to restricted biological databases. Sensitive human genomic and medical information requires appropriate legal, consent, security and access controls.

This layer does not provide instructions for creating pathogens, modifying harmful biological agents, or bypassing biosafety controls.

## 10. Integration with World Knowledge

```text
IEEE / Engineering
        |
        v
Electronics -> Sensors -> Instruments -> Networks
        |
        +-------------------+
                            v
                      Scientific Data
                            |
       +--------------------+-------------------+
       v                    v                   v
   Genomics             Proteins           Species
       |                    |                   |
       +--------------------+-------------------+
                            v
                       Knowledge Graph
                            |
                            v
                          ORBIT
```

## 11. Registry families
- IEEE technology registry
- Blood/transfusion registry
- Genomics registry
- Biobank registry
- Species/biodiversity registry
- Protein registry
- Molecular/structure registry
- Scientific publication/evidence registry

## 12. Implementation roadmap
Phase 1: schemas, canonical IDs, source registry and provenance.
Phase 2: public metadata ingestion and identifier crosswalks.
Phase 3: evidence/knowledge graph and temporal versioning.
Phase 4: search, visualization and data-gap detection.

Completion requires source validation, license review, provenance, versioning, tests and operational monitoring.
