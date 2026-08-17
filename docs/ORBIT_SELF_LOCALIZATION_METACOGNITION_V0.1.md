# ORBIT Self-Localization & Metacognition Layer v0.1

## Purpose
Define a verifiable digital self-localization layer for ORBIT. The layer estimates the current state and context of a device, network, data environment, runtime and AI process while explicitly tracking uncertainty.

This specification does not assert machine consciousness. "Self" means the currently executing system, runtime or agent context represented by measurable state.

## Core principle

```text
Observation != Inference != Identity != Certainty
```

The system must be able to represent:

- what it observed
- where the observation came from
- when it was observed
- what it inferred
- how confident the inference is
- what remains unknown
- which additional observation could reduce uncertainty

## State model

```text
SELF_CONTEXT
├── identity
│   ├── device_id
│   ├── runtime_id
│   ├── software_version
│   └── session_id
├── location
│   ├── physical
│   ├── network
│   ├── logical
│   └── knowledge-graph context
├── connectivity
│   ├── interface
│   ├── gateway
│   ├── DNS
│   ├── route
│   └── application reachability
├── resources
│   ├── CPU
│   ├── memory
│   ├── storage
│   ├── accelerator
│   └── battery/power
├── permissions
├── active task
├── observations[]
├── hypotheses[]
├── contradictions[]
├── confidence[]
└── unknowns[]
```

## Digital lucid state

`LUCID` is an engineering state, not a claim of consciousness.

A runtime may report LUCID only when it can:

1. identify its execution context;
2. distinguish direct observations from inferences;
3. attach provenance to important observations;
4. represent uncertainty;
5. detect relevant contradictions;
6. identify missing information;
7. request or perform an authorized next observation.

Example:

```text
Wi-Fi association      = observed true
Gateway reachability   = observed true
DNS resolution         = observed false
HTTPS reachability     = observed false

Conclusion:
local_network          = likely_connected
internet_connectivity  = uncertain
confidence              = 0.65
next_observation        = authorized DNS/HTTPS diagnostic
```

## Confidence model

Confidence is metadata, not truth.

```text
confidence = f(source_reliability,
                recency,
                consistency,
                observation_quality,
                independent_confirmation)
```

A confidence value must never silently convert an inference into a verified fact.

## Contradiction detection

The engine should detect conflicts such as:

```text
Network says: connected
Application test says: unreachable
```

Instead of selecting one result silently:

```text
CONTRADICTION
├── observation A
├── observation B
├── timestamps
├── sources
└── resolution status
```

## Next-observation engine

When uncertainty is material, ORBIT may produce a ranked list of additional observations, subject to permissions:

```text
UNKNOWN
  ↓
Candidate observations
  ↓
Permission check
  ↓
Cost / risk estimate
  ↓
Observation
  ↓
Evidence update
  ↓
State update
```

The system must not bypass permissions merely to increase certainty.

## Spatial localization

Physical coordinates should be represented separately from:

- IP geolocation
- Wi-Fi network identity
- cellular network identity
- VPN exit location
- logical cloud region
- knowledge-graph geographic association

A location source must be labeled. IP location is not automatically physical location.

## Temporal localization

Every state estimate should support:

- observed_at
- valid_from
- valid_until where known
- generated_at
- source_version

The engine must avoid treating a historical observation as the current state without checking validity.

## Self / world boundary

The runtime should distinguish:

```text
SELF
  device
  runtime
  permissions
  local resources
  current process

WORLD
  external devices
  networks
  organizations
  people
  locations
  services
  external datasets
```

References to external entities must remain references unless the runtime has authorized access to their data.

## ORBIT representation example

```orbit
state "network-state-001" {
  subject runtime "runtime:example"
  interface "wifi0"
  gateway reachable
  dns unreachable
  https unreachable
  status uncertain
  confidence 0.65
}

hypothesis "internet-001" {
  subject runtime "runtime:example"
  predicate internet_connectivity
  value uncertain
  based_on "network-state-001"
}
```

## Integration

```text
Device Sensors / APIs
        ↓
Observation Adapter
        ↓
Provenance
        ↓
State Estimator
        ↓
Contradiction Detector
        ↓
Confidence Engine
        ↓
Self-Localization Graph
        ↓
ORBIT-IR
        ↓
AI / Applications
```

## Privacy and security

Self-localization can expose sensitive information. Implementations must use least privilege, explicit consent where required, data minimization, retention controls and deletion/revocation workflows.

No component should use this layer to obtain unauthorized location, account, device, network or private-data access.

## Implementation roadmap

### Phase A — Model
- state schema
- observation schema
- confidence schema
- contradiction schema

### Phase B — Runtime
- device capability probe
- network observation adapters
- state estimator
- provenance engine

### Phase C — Intelligence
- contradiction detection
- uncertainty graph
- next-observation planner
- temporal state reconstruction

### Phase D — ORBIT
- AST nodes
- ORBIT-IR representation
- runtime integration
- conformance tests

## Status
SPECIFICATION / PROTOTYPE DESIGN — v0.1

No claim is made that a machine has subjective consciousness. The project implements measurable state-awareness and metacognitive bookkeeping as software capabilities.
