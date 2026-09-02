# Specialized Skill Routing

Load specialized skills only when task signals justify them.

| Signal | Route |
|---|---|
| authentication, authorization, secrets, crypto | secure-coding/security |
| REST/GraphQL/event contract | API design |
| React, CSS, UI state, accessibility | frontend |
| Spring Boot, FastAPI, service layer | backend |
| schema, migration, SQL, data contract | database/data engineering |
| PII, regulated data, audit | compliance/privacy |
| CI/CD, release, Kubernetes, cloud | platform/deployment |
| flaky tests, coverage, verification | testing |
| metrics, traces, SLO | observability |

Avoid broad fan-out. The orchestrator owns lifecycle state and artifact integrity; specialized skills own domain rules.
