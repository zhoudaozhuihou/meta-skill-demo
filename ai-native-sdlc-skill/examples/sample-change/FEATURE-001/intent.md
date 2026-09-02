# Intent

## Change ID

`FEATURE-001`

## Problem

Authenticated users currently need multiple UI/API requests to understand their account status and basic profile summary.

## Desired Outcome

Provide one read-only account summary contract for the authenticated user.

## Users / Actors

Authenticated end users and the first-party web application.

## Scope

- read-only summary endpoint;
- current user's own data only;
- existing authentication remains authoritative.

## Out of Scope

- account updates;
- administrative lookup;
- cross-user access.

## Constraints

No password hash, secret, credential, or internal-only security field may be exposed.

## Success Criteria

- authenticated users receive their own summary in one request;
- unauthenticated access is rejected;
- ownership and response-field behavior have regression tests.

## Known Context

Use existing authentication middleware and repository API conventions.

## Open Questions

None.

## Risks

Authorization/field-selection mistakes could expose another user's data or sensitive fields.
