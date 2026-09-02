# Gating and Rollback

## Default policy

Accept only strict validation improvement:

```python
accepted = candidate_score > best_score
```

This mirrors the research algorithm.

## Candidate isolation

Never patch the accepted active skill set in-place before validation.

Recommended:

```text
accepted skills/
      │
      ├── clone
      ▼
candidate workspace
      │
      ├── apply proposal
      ├── validate
      ▼
gate
```

## Accepted

1. promote candidate;
2. persist new best score;
3. record diff and outcome.

## Rejected

1. discard candidate skill changes;
2. keep accepted skills unchanged;
3. keep wiki unchanged/updated;
4. record rejection and diff.

## Production adaptation

A real system may add safety constraints:

```text
metric improvement
AND no policy regression
AND no critical eval regression
AND approval satisfied
```

Do not silently replace the paper-faithful metric rule; document any stricter production gate.
