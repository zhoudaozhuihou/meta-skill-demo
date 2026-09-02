# Specification

## Change ID

`FEATURE-001`

## Context

The application already authenticates users and exposes account/profile data through separate internal paths.

## Current State

The UI aggregates multiple calls and there is no single self-summary contract.

## Target State

A read-only endpoint returns a documented allowlisted summary for the authenticated identity.

## Functional Requirements

1. Reject unauthenticated requests.
2. Resolve account identity from trusted authentication context, never a caller-supplied user ID.
3. Return only allowlisted summary fields.
4. Return repository-standard not-found/disabled behavior when appropriate.

## Non-Functional Requirements

### Performance

No materially more expensive data access than existing account lookup.

### Security

Ownership is implicit in authenticated identity. Sensitive credential/security fields are excluded.

### Reliability

No write-side effects.

### Accessibility

Not applicable to the API contract itself.

### Observability

Use existing request/error telemetry without logging sensitive response payloads.

### Compliance / Privacy

Return the minimum fields needed by the first-party UI.

## Architecture

Reuse existing authentication middleware, service/repository access patterns, and response serialization conventions.

## Components

Router/controller, account service, response DTO/schema, tests.

## Data Flow

Authenticated identity → account service lookup → allowlisted response schema → client.

## API / Interface Changes

Add a read-only current-account summary route following repository naming/versioning conventions.

## Data Model / Schema Changes

None.

## UI / UX Behavior

The UI may replace multiple summary requests with the new endpoint.

## Failure Scenarios

Unauthenticated, missing account, disabled account, dependency failure.

## Compatibility

Additive API change.

## Migration Strategy

Ship endpoint first; migrate UI separately if desired.

## Acceptance Criteria

- [ ] unauthenticated request is rejected
- [ ] authenticated request is scoped to current identity
- [ ] sensitive fields are absent
- [ ] regression tests cover auth and field selection

## Risks and Trade-offs

A convenience endpoint can become over-broad over time; keep an explicit response schema.

## Open Decisions

Exact route naming follows repository conventions discovered during planning.
