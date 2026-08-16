# AI Observation Protocol v0.1

## Purpose

Provide a common method for AI systems to analyze photographs, maps, documents, products, buildings, roads and economic observations without confusing visual guesses with verified facts.

## Analysis sequence

1. **Observe** — list only what is directly visible or explicitly measured.
2. **Identify** — propose object, building, road, product or land-use classifications.
3. **Locate** — attach coordinates and geographic context when available.
4. **Contextualize** — describe surrounding land use, population, mobility and commercial context.
5. **Source** — retrieve independent public or authorized evidence.
6. **Connect** — map relationships to manufacturers, suppliers, resources, transport and markets.
7. **Quantify** — calculate unit prices, distances, densities, capacities and other derived measures.
8. **Assess quality** — evaluate durability, material, condition, repairability and lifecycle only when evidence supports the assessment.
9. **Check alternatives** — actively search for competing explanations.
10. **Report uncertainty** — clearly label observed, sourced, derived, inferred and unknown information.

## Required output distinction

AI responses should separate:

### Observed
Directly visible, measured or explicitly supplied information.

### Sourced
Information supported by a named source or authorized dataset.

### Derived
Mathematical or logical results reproducible from cited inputs.

### Inferred
A reasoned interpretation that remains uncertain.

### Unknown
Information for which reliable evidence is currently unavailable.

## Evidence discipline

Do not convert a probability into a fact. Do not infer private identity from appearance. Do not expose private personal information. Do not treat correlation as causation. Preserve timestamps and source provenance.

## Product analysis

For a physical product, attempt to identify:

- product category
- brand/model when visually supported
- specification and quantity
- local observed price
- normalized unit price
- origin/manufacturer when independently supported
- materials
- manufacturing process when sourced
- supply-chain relationships
- estimated resource inputs
- lifecycle, repair and recycling characteristics

Production cost and profit must be labeled as estimates unless supported by reliable cost data.

## Spatial analysis

For a coordinate or image, analyze:

- residential areas
- commercial areas
- markets
- industrial areas
- agriculture
- protected/reserved land when data exists
- pedestrian routes
- bicycle routes
- motorcycle routes
- car routes
- freight routes
- public transport
- rail, ports and airports
- utilities and public infrastructure

Explain possible design relationships without claiming intent unless planning evidence exists.

## Historical analysis

Compare observations across time. Record what changed, when it changed, and what evidence supports each transition. Separate documented causes from hypotheses.

## Forensic-inspired reasoning

Use:

`observation → evidence → hypothesis → corroboration → alternatives → conclusion → revision`

The goal is disciplined reconstruction, not automatic accusation or legal judgment.

## Global collaboration

AI systems and human contributors may independently analyze the same observation. Their outputs should remain attributable, versioned and comparable. Agreement between models is not itself proof.
