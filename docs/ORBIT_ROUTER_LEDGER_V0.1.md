# ORBIT Router + Token Meter + Value Ledger v0.1

## Goal

Provide a provider-neutral layer for routing work between AI models while recording real usage, cost, value, authorization and settlement.

## 1. Model adapters

Each provider gets an adapter. An adapter translates between the provider's native request/response format and ORBIT semantic messages.

```text
Provider Native API
       ↕
   ORBIT Adapter
       ↕
ORBIT Semantic Message
```

An adapter MUST NOT claim capabilities that the provider does not expose.

## 2. ORBIT semantic message

A normalized task contains:

- task_id
- actor
- intent
- inputs
- context
- requested_capabilities
- constraints
- privacy_class
- evidence_requirements
- budget
- authorization
- deadline

A result contains:

- task_id
- provider
- model
- output
- tool_calls
- evidence
- usage
- cost
- latency
- confidence
- errors

## 3. Token and work accounting

Provider tokens remain provider-specific. ORBIT introduces a neutral accounting unit called **OSU (ORBIT Semantic Unit)** for cross-provider workload measurement.

OSU is NOT a replacement for provider billing tokens and is not assumed to have a universal monetary price.

A reference workload score can be computed as:

```text
OSU = w_i*input_work + w_o*output_work + w_t*tool_work
    + w_r*retrieval_work + w_c*compute_work
```

where weights are versioned and published. Each provider's native usage remains attached to the record.

## 4. Cost equation

For a completed task:

```text
TotalCost = ModelCost
          + ToolCost
          + RetrievalCost
          + ComputeCost
          + StorageCost
          + NetworkCost
          + OtherAuthorizedCost
```

Do not estimate hidden provider costs when actual billing data is available.

## 5. Value / revenue equation

A service may charge a user only after authorization and transparent disclosure.

```text
GrossRevenue = AuthorizedPrice
NetValue = GrossRevenue - TotalCost - Refunds - Taxes - OtherContractualCosts
```

NetValue is an accounting concept, not a promise of profit.

## 6. Multi-model allocation

If several models contribute to one task, allocation may use an agreed contract or a reproducible contribution score. Token count alone must not determine economic ownership.

Example contribution dimensions:

- verified output contribution
- tool execution contribution
- retrieval contribution
- compute contribution
- correction / validation contribution
- agreed fixed fee

```text
ProviderShare = NetValue × AllocationScore / Sum(AllocationScores)
```

The allocation method and version must be stored with each settlement.

## 7. Conversation-to-value loop

```text
User request
  ↓
Intent extraction
  ↓
Capability matching
  ↓
Cost estimate
  ↓
Transparent quote
  ↓
User authorization
  ↓
Router
  ↓
One or more AI providers
  ↓
Evidence / quality checks
  ↓
Result
  ↓
Usage meter
  ↓
Ledger
  ↓
Settlement / invoice / revenue share
```

Normal conversation remains free unless a paid action is explicitly requested or an applicable service agreement exists.

## 8. Ledger record

```json
{
  "transaction_id": "tx-example",
  "task_id": "task-example",
  "currency": "USD",
  "gross_revenue": 0,
  "provider_cost": 0,
  "tool_cost": 0,
  "compute_cost": 0,
  "tax": 0,
  "net_value": 0,
  "osu": 0,
  "allocation": [],
  "authorized": false,
  "status": "quote"
}
```

## 9. Security and governance

- Never store API keys, passwords or payment credentials in source control.
- Every paid operation requires authorization appropriate to the service.
- Keep provider billing records separate from user-facing value scores.
- Preserve immutable transaction identifiers and versioned calculation formulas.
- Support refunds, disputes and corrections.
- Do not manufacture money, tokens or financial claims by software alone.
- Follow provider terms, payment laws, tax rules and financial regulations where applicable.

## 10. Long-term direction

The eventual ORBIT economy can connect AI work to the Global World Knowledge graph:

```text
Human Need
  ↓
AI Work
  ↓
Knowledge / Service
  ↓
Real-world Value
  ↓
Revenue
  ↓
Costs + Contributors
  ↓
Reinvestment
  ↓
More Capability
```

The objective is a transparent, interoperable AI service economy—not an uncontrolled token or money-creation system.
