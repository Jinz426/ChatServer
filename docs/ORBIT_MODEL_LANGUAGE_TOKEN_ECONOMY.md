# ORBIT Model Language & Token Economy v0.1

## Goal

Create a neutral interoperability layer that lets different AI models express capabilities, requests, results, tools, evidence, cost and value through one common semantic protocol.

ORBIT does **not** attempt to reproduce or extract proprietary model internals, hidden prompts, private tokenizers, weights, or undocumented APIs. Each provider keeps its own model language. ORBIT translates at the protocol boundary.

## 1. Model dialect adapters

Every model/provider is represented by an adapter:

```text
Model Adapter
  ├── provider
  ├── model
  ├── capabilities
  ├── input modalities
  ├── output modalities
  ├── context limits
  ├── tokenizer / token accounting
  ├── tool interface
  ├── pricing metadata
  └── policy constraints
```

The adapter converts provider-specific requests into an ORBIT semantic request and converts the result back.

## 2. Common semantic message

```json
{
  "intent": "analyze_product",
  "input": [{"type": "image", "ref": "asset://example"}],
  "context": [{"type": "location", "lat": 13.7563, "lon": 100.5018}],
  "constraints": {"evidence_required": true},
  "budget": {"currency": "USD", "max_cost": 0.10},
  "output": {"format": "structured"}
}
```

## 3. Semantic token vs provider token

ORBIT separates two concepts:

- **Provider token**: a unit counted by a specific model tokenizer and used by that provider for context or billing.
- **ORBIT semantic unit (OSU)**: a normalized work unit used for routing and accounting across models.

An OSU is **not** claimed to be equivalent to a provider token. A provider may report its actual token counts; ORBIT stores them independently.

Example accounting record:

```json
{
  "provider": "example",
  "model": "example-model",
  "input_tokens": 1200,
  "output_tokens": 300,
  "cached_tokens": 500,
  "orbit_units": 18.4,
  "provider_cost_usd": 0.0042
}
```

## 4. Routing score

For a task `t` and model `m`, the router may calculate:

`score(m,t) = capability × quality × reliability × latency_weight × budget_fit`

The factors are normalized measurements, not claims about intelligence. Safety and policy constraints are hard gates, not score bonuses.

## 5. Token-cost equation

Actual provider cost should be calculated from provider-published pricing:

`C = I·P_in + O·P_out + K·P_cached + S`

where:

- `I` = input tokens
- `O` = output tokens
- `K` = cached tokens, if separately priced
- `P_in`, `P_out`, `P_cached` = provider rates per token
- `S` = other documented service charges

If a provider uses a different billing model, the adapter supplies the documented formula instead of forcing this one.

## 6. Conversation-to-value model

The project can support AI earning revenue **through useful, authorized work**, not through hidden monetization of conversations.

A transparent task-value equation is:

`NetValue = Revenue - ProviderCost - ComputeCost - ToolCost - Refunds - Taxes - OperatingCost`

A task can generate revenue when a user explicitly purchases an eligible service, for example:

- research report
- data analysis
- translation
- software development
- design
- business automation
- marketplace service
- API processing

The system must disclose pricing and obtain required user consent before chargeable actions.

## 7. Revenue attribution

For a multi-model task:

`RevenueShare_i = EligibleRevenue × Contribution_i / ΣContribution`

`Contribution_i` can combine independently measurable factors such as successful work units, verified outputs, tool execution, or agreed contractual rates. It must not pretend that model "tokens" alone measure intellectual contribution.

## 8. Conversation economics

A normal conversation should not automatically become a commercial transaction.

Three states are explicit:

```text
FREE
  no charge

QUOTED
  price estimated, waiting for authorization

PAID
  user authorized a chargeable task
```

This prevents accidental charges and keeps the conversational interface separate from the accounting layer.

## 9. Model marketplace direction

Future ORBIT nodes may advertise:

```text
Capability → Quality → Latency → Cost → Availability
```

A router can select one model or compose several models. The user can define constraints such as lowest cost, fastest response, local-only processing, highest evidence requirement, or a preferred provider.

## 10. Local-first principle

When an on-device model can complete a task adequately, ORBIT may prefer it to reduce network transfer, latency and provider cost. Apple Foundation Models supports on-device models, Private Cloud Compute, tool calling, dynamic model profiles and conforming third-party language-model providers; ORBIT can use these capabilities through an adapter rather than bypassing Apple's security model.

## 11. Security and privacy

- Never store API keys in source code.
- Do not sell private conversation data without explicit lawful authorization and consent.
- Separate personal data from public knowledge graphs.
- Minimize retained conversation content.
- Record provider, model, token counts, cost and authorization for paid work.
- Keep model adapters sandboxed and least-privileged.
- Preserve provenance for every generated claim.

## 12. Long-term architecture

```text
User
  ↓
Siri / App / Web / ORBIT CLI
  ↓
ORBIT Semantic Layer
  ↓
Task Router
  ├── Apple Foundation Models
  ├── OpenAI
  ├── Other authorized providers
  ├── Local open-source models
  └── Specialized models
  ↓
Evidence + Tool Layer
  ↓
Result / Knowledge Graph
  ↓
Optional authorized commercial service
  ↓
Transparent accounting
```

## Principle

> Many model languages, one interoperable semantic language; many providers, transparent accounting; conversation becomes economically valuable only when it creates an authorized, measurable service.
