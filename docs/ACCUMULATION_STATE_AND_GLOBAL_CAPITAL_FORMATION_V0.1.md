# Accumulation State & Global Capital Formation v0.1

## Purpose
Model how starting endowments and subsequent accumulation affect people, households, firms, cities and states. The model is intended for observation, comparison, simulation and policy research; it must not assume that wealth inequality has one cause.

## Core hypothesis
Initial accumulation can create path dependence: an entity entering an economic cycle with more productive assets, human capital, infrastructure, knowledge, credit access or institutional capacity may have more opportunities to generate and reinvest surplus.

This is a hypothesis to test empirically, not a universal causal conclusion.

## Accumulation state

```text
ACCUMULATION_STATE
├── Financial Capital
├── Physical Capital
├── Human Capital
├── Knowledge / Intellectual Capital
├── Social Capital
├── Institutional Capital
├── Natural Capital
├── Infrastructure Access
├── Technology Access
├── Credit Access
├── Time / Care Resources
├── Inherited / Transferred Assets
├── Debt / Liabilities
├── Risk Exposure
├── Income / Cash Flow
├── Saving Rate
├── Reinvestment Rate
├── Return on Assets
└── Time Horizon
```

## Levels

### Individual
Record only authorized and privacy-preserving aggregate data where appropriate:
- assets and liabilities
- education / skills
- employment and income bands
- access to financial services
- housing / productive-asset ownership
- technology access
- transfers and inheritance where legally available as aggregate statistics

### Household
- combined assets/liabilities
- housing and productive assets
- household income and expenditure
- intergenerational transfers
- education and care resources
- credit access

### Firm
- equity and debt capital
- physical capital
- intellectual property
- human capital
- brand / customer assets where measurable
- cash flow
- reinvestment
- financing cost
- market access

### City / Region
- infrastructure stock
- land and housing
- education and health systems
- industrial base
- logistics connectivity
- financial access
- technology ecosystem
- public capital

### Country / State
- physical capital
- public infrastructure
- natural-resource endowment
- human capital
- institutional capacity
- domestic savings
- financial-system depth
- fiscal capacity
- external assets/liabilities
- technology capacity
- trade and market access

## Dynamic model

```text
Initial Endowment
       ↓
Production Capacity
       ↓
Income / Surplus
       ↓
Consumption + Saving
       ↓
Investment
       ↓
Asset Stock
       ↓
Productivity / Return
       ↓
New Endowment
       ↺
```

The model should allow shocks:
- recession
- inflation
- disaster
- war
- policy change
- technological change
- illness / care burden
- migration
- demographic change
- financial crisis

## Distribution analysis
Measure more than wealth totals:
- median and mean wealth
- wealth shares
- income distribution
- asset ownership concentration
- debt burden
- intergenerational mobility
- access to productive capital
- financing cost
- opportunity access
- regional disparities

Use source-specific definitions and avoid comparing incompatible indicators without normalization.

## Capital formation objective
The system can study mechanisms that increase broad productive capacity:

1. Basic security and essential infrastructure
2. Education and skill formation
3. Health and human-capital development
4. Affordable financial access
5. Productive-asset ownership opportunities
6. Small-business formation
7. Technology and knowledge access
8. Infrastructure connectivity
9. Fair and transparent institutions
10. Long-term reinvestment

The objective is not to equalize every outcome. It is to investigate how barriers to productive participation can be reduced while preserving voluntary ownership, lawful markets and individual agency.

## Simulation layer

Future simulations should compare scenarios rather than prescribe one universal policy:

```text
Scenario
  ↓
Initial distribution
  ↓
Policy / technology / shock
  ↓
Behavioral response
  ↓
Investment
  ↓
Productivity
  ↓
Distribution after N periods
```

Every simulation records assumptions, parameter ranges, uncertainty and sensitivity analysis.

## Causal discipline
Separate:
- observation
- correlation
- causal hypothesis
- mechanism
- model assumption
- simulation result
- policy recommendation

Do not infer causality merely from wealth correlation.

## Privacy
Individual-level financial, health, location and family data can be highly sensitive. The global knowledge system should prefer public aggregates, consented records, anonymization and data minimization. No person should be assigned a wealth or social score without a legitimate, transparent purpose and appropriate governance.

## Integration with ORBIT

```text
Person / Household / Firm / City / Country
                 ↓
        ACCUMULATION_STATE
                 ↓
      Observation + Provenance
                 ↓
          ORBIT entities
                 ↓
      Economic relationship graph
                 ↓
        Simulation / ML models
                 ↓
      Evidence + uncertainty
```

## Status
ARCHITECTURE / RESEARCH SPECIFICATION — v0.1

This document does not claim that a complete global individual-level dataset exists or should be created. Population-scale analysis should use lawful, privacy-preserving and source-appropriate data.
