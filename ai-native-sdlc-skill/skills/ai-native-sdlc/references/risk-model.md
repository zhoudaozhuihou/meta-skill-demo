# Risk Model

Risk is evaluated across impact and reversibility.

Questions:

- Can this expose or corrupt customer/regulated data?
- Can this weaken authentication or authorization?
- Can it cause destructive or irreversible data changes?
- Does it modify production infrastructure or deployment controls?
- Does it change public contracts or downstream integrations?
- Is rollback expensive or ambiguous?
- Is the affected surface business-critical?

Controls should increase with risk: stronger artifacts, tests, independent review, migration/rollback plans, and approvals.
