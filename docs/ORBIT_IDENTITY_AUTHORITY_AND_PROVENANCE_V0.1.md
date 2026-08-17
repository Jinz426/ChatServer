# ORBIT Identity, Authority & Provenance v0.1

## Purpose
Define a consent-first identity and provenance layer for cameras, microphones, files, metadata, contributions and relationships. The design may recognize an authorized owner/operator of a device or workspace, but it must never claim ownership of a person without explicit consent and lawful authority.

## Core principle

> Identity should establish who authorized an action; provenance should establish what happened; contribution records should establish what was contributed; authority should establish what the system is allowed to do.

Do not collapse identity, ownership, contribution, authorship, control, or legal title into one field.

## Device and sensor observation

```text
Camera / Microphone / File / Sensor
        ↓
Consent + Permission Check
        ↓
Capture Event
        ↓
Raw Observation
        ↓
Metadata Extraction
        ↓
Provenance Record
        ↓
Local / Authorized Knowledge Index
```

Supported observation classes may include:
- image
- audio
- video
- document
- sensor observation
- device state
- network event
- application event

The system must clearly distinguish raw data from derived metadata and model inference.

## Metadata and provenance

Track, where available and lawful:
- creation timestamp
- modification timestamp
- device/application identifier
- file type and size
- cryptographic hash
- capture context
- source
- transformation history
- model/version used for processing
- consent scope
- retention policy

Do not collect hidden metadata merely because it exists. Apply data minimization and explicit permission rules.

## Contribution graph

```text
Actor
 ↓
Contribution
 ↓
Artifact / Observation / Decision
 ↓
Transformation
 ↓
Downstream use
 ↓
Attribution / Credit
```

Contribution records can represent:
- authorship
- research contribution
- code contribution
- dataset contribution
- financial contribution
- operational contribution
- maintenance
- review
- infrastructure

A contribution record does not automatically establish legal ownership or entitlement.

## Relationship graph

Use typed relationships rather than an unrestricted hierarchy:

```text
Entity A ──[relationship type]──> Entity B
```

Examples:
- owns
- operates
- employs
- governs
- funds
- contributes_to
- authored
- maintains
- supplies
- depends_on
- collaborates_with
- represents
- licenses
- regulates

Each relationship should include source, timestamp, confidence and applicable authority.

## Hierarchy and authority

Hierarchies can arise naturally in organizations and technical systems, but the model must distinguish:

1. structural hierarchy
2. functional leadership
3. legal authority
4. operational control
5. resource access
6. social influence
7. technical permission

A position of influence does not automatically grant technical or legal authority.

Where no governance exists, the system should not manufacture arbitrary personal authority. Instead it should create explicit, reviewable rules for the relevant domain.

## Electrical / power systems

For energy infrastructure, model authority and dependency explicitly:

```text
Generation
   ↓
Transmission
   ↓
Distribution
   ↓
Meter / Storage
   ↓
Device
   ↓
Load
```

Track:
- operator
- owner where legally established
- connection point
- capacity
- protection state
- dependency
- outage state
- authorization
- safety constraints

The software must never bypass electrical protections or safety controls merely to obtain more device power or control.

## Device control model

“Maximum capability” means maximizing lawful, measurable performance within hardware and safety constraints—not unrestricted privilege.

```text
Capability Probe
 ↓
Permission Check
 ↓
Safety Policy
 ↓
Resource Budget
 ↓
Task Execution
 ↓
Telemetry
 ↓
Verification
```

Prefer official OS APIs, sandboxed permissions, user-visible controls and hardware safety limits.

## iPhone / Apple integration concept

For an Apple device, the integration layer should prefer supported mechanisms such as:
- camera and microphone permission APIs
- App Intents / Shortcuts where available
- local file providers
- Core ML / Vision where appropriate
- system metadata APIs exposed to applications
- secure local storage
- explicit user authorization

The model must not attempt to defeat iOS security, sandboxing, privacy indicators, passcodes, encryption or hardware protections.

## “Owner mode” / Authorized Principal Mode

Use the safer concept of **Authorized Principal Mode** rather than an absolute ownership mode.

```text
User verifies identity
        ↓
Selects device / workspace
        ↓
Chooses permissions
        ↓
Consent recorded
        ↓
Capability profile activated
        ↓
Every sensitive action checked
```

Permissions should be granular:
- camera: deny / ask / allow for selected function
- microphone: deny / ask / allow for selected function
- files: selected files/folders only where supported
- location: selected scope
- network: application/system policy
- automation: explicit action scope

## Security requirements

- least privilege
- explicit consent
- revocation
- audit logs
- cryptographic integrity
- secure key storage
- rate limits
- sandboxing
- fail-safe behavior
- no covert capture
- no hidden persistence

## Evidence model

Every important assertion should be traceable:

```text
Claim
 ↓
Evidence
 ↓
Source
 ↓
Timestamp
 ↓
Transformation
 ↓
Confidence
 ↓
Current validity
```

## Integration with ORBIT

```text
Authorized Identity
        ↓
Capability Profile
        ↓
Observation
        ↓
Metadata
        ↓
Provenance
        ↓
Contribution Graph
        ↓
Relationship Graph
        ↓
Functional Leadership
        ↓
Reference Frontier
```

## Governance principle

The strongest system is not the one with unrestricted access. It is the one that can reliably determine:

- who authorized an action
- what the action is allowed to access
- why it is needed
- what evidence resulted
- who contributed
- what changed
- how the action can be revoked

## Status
ARCHITECTURE / RESEARCH SPECIFICATION — v0.1
