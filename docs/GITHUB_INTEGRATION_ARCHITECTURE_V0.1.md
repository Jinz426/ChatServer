# GitHub Integration Architecture v0.1

## Purpose
Translate the current GitHub integration concepts into an implementation plan for the ORBIT project.

GitHub documents integrations as tools that extend GitHub functionality. The principal building blocks include GitHub Apps, GitHub Actions workflows, custom Actions, APIs, webhooks, and—where appropriate—Marketplace distribution. Source: https://docs.github.com/en/integrations/concepts/about-building-integrations

## Architecture

```text
GitHub Repository
      │
      ├── GitHub App / authenticated integration
      │        ↓
      │   REST API / GraphQL API
      │        ↓
      │   ORBIT Integration Layer
      │        ↓
      │   Knowledge / Runtime / Evidence systems
      │
      ├── Webhooks
      │        ↓
      │   Event Router
      │        ↓
      │   Validation → Queue → Worker → Result
      │
      └── GitHub Actions
               ↓
          CI / tests / validation / packaging
```

## Integration roles

### GitHub App
Use when ORBIT needs a durable, permission-scoped integration that acts on repositories or installations. Keep permissions minimal and explicit.

### GitHub Actions
Use repository events to automate reproducible workflows such as:
- linting
- schema validation
- unit/integration tests
- documentation checks
- data-source manifest validation
- build/package verification
- release preparation

### Custom Actions
Use reusable actions when a workflow capability should be packaged for repeated use.

### REST and GraphQL APIs
Use the API layer for controlled reads and writes. Prefer the narrowest API and permission scope required by each operation.

### Webhooks
Use signed, validated event delivery to react to repository events. Events should enter a queue/event router before expensive processing.

## ORBIT event model

```text
GitHub Event
   ↓
Authenticate / verify signature
   ↓
Normalize event
   ↓
Assign event ID + timestamp
   ↓
Check idempotency
   ↓
Policy / permission check
   ↓
Queue
   ↓
Worker
   ↓
Evidence + audit record
   ↓
GitHub result / external result
```

## Security principles

1. Least privilege.
2. Separate read and write capabilities.
3. Never place secrets in source files, commits, issues, or logs.
4. Verify webhook authenticity before processing.
5. Make write operations auditable and reversible where possible.
6. Use idempotency keys/event IDs to prevent duplicate processing.
7. Separate user-authorized data from public repository data.
8. Record which integration identity performed each action.
9. Version integration configuration and schemas.
10. Fail closed when permissions or provenance cannot be verified.

## Permission model

ORBIT should define capability scopes such as:

```text
repo.read
repo.write
issues.read
issues.write
pull_requests.read
pull_requests.comment
actions.read
artifacts.read
metadata.read
webhooks.receive
```

Actual GitHub permissions must be mapped to the minimum GitHub App permissions required by the implementation. Do not request broad permissions merely for convenience.

## Provenance

Every automated repository change should record:
- event ID
- actor / integration identity
- repository
- branch/ref
- source commit
- operation
- files changed
- validation status
- timestamp
- tool/version
- reason or triggering event

## AI integration

If generative AI is used, AI-generated changes must pass deterministic checks before merge or release. AI should be treated as an assisting component, not as an implicit authorization mechanism.

Recommended flow:

```text
Event
 ↓
AI analysis / proposal
 ↓
Policy checks
 ↓
Deterministic tests
 ↓
Human or pre-authorized review gate
 ↓
Write / PR
 ↓
Post-change verification
```

## Repository maintenance

The ORBIT repository should maintain:
- canonical documentation paths
- machine-readable schemas
- source registry
- license/NOTICE registry
- test suites
- workflow definitions
- changelog
- security policy
- contribution guidance
- integration configuration templates

## Failure handling

The integration must distinguish:
- authentication failure
- authorization failure
- missing resource
- stale revision / SHA conflict
- validation failure
- rate limiting
- transient network failure
- webhook duplication
- external provider failure

Retries must be bounded and safe. Never blindly retry non-idempotent writes.

## Scope boundary

This specification does not grant ORBIT unrestricted access to GitHub, other networks, private repositories, or user data. Access remains bounded by the permissions, installation, authorization, policies and legal terms applicable to the integration.

## Roadmap

1. Define GitHub App permissions.
2. Define webhook event allowlist.
3. Implement event normalization and idempotency.
4. Add CI validation workflows.
5. Add repository/documentation health checks.
6. Add audit/provenance records.
7. Add controlled AI proposal workflow.
8. Add release automation.
9. Evaluate Marketplace publication only after security and operational maturity.

## Status
ARCHITECTURE / IMPLEMENTATION SPECIFICATION — v0.1

Reference: GitHub Docs, “About building integrations,” current documentation accessed during project maintenance.
