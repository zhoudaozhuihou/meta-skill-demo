# Implementation Plan

## Change ID

`FEATURE-001`

## Summary

Add an additive current-account summary API using existing authentication and account access patterns.

## Files to Add

Determine exact test/DTO files after repository inspection.

## Files to Modify

Determine router/controller and service files after repository inspection.

## Files to Remove

None.

## Implementation Sequence

### Step 1
Inspect authentication middleware, existing current-user endpoints, account service, response schemas, and test conventions.

### Step 2
Define an explicit allowlisted summary response schema and authenticated route.

### Step 3
Reuse service/repository lookup scoped to trusted authenticated identity.

### Step 4
Add tests for unauthenticated rejection, ownership, expected fields, and sensitive-field exclusion.

## Interfaces / Contracts

Additive read-only API contract. Do not accept arbitrary user ID for this endpoint.

## Database Changes

None expected.

## Configuration Changes

None expected.

## Dependency Changes

None expected.

## Security Considerations

Security review required because authorization and sensitive-field selection are involved.

## Compatibility Considerations

Additive endpoint; existing clients remain unchanged.

## Tests

### Unit
Response schema/serializer and service behavior if repository convention supports it.

### Integration
Authenticated/unauthenticated route and ownership behavior.

### End-to-End
Only if existing project E2E suite covers account summary flows.

### Regression
No sensitive credential/security fields in response.

## Verification

Discover actual build, lint, and test commands from repository instructions/CI before implementation completion.

## Risks

Incorrect identity source or overly broad serialization.

## Rollback Strategy

Remove/disable additive route if not yet consumed; no data migration required.

## Definition of Done

- [ ] route uses trusted authenticated identity
- [ ] explicit response allowlist
- [ ] auth/ownership tests pass
- [ ] security review has no unresolved required finding
