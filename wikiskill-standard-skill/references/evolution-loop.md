# WikiSkill Evolution Loop

State:

```text
S_k = active skill set at iteration k
W_k = persistent wiki at iteration k
Rbest = best accepted validation score
```

Algorithm:

```text
initialize S0
initialize W0
evaluate S0 on validation -> Rbest

for each iteration k:
    run training rollouts using S(k-1)
    sample success/failure traces
    update persistent wiki -> W'
    propose one atomic skill change Pk
    apply Pk -> candidate S'
    evaluate candidate S' on validation

    if candidate_score > Rbest:
        accept S'
        update Rbest
    else:
        rollback to S(k-1)

    append proposal + diff + score + decision to wiki/skill-impact.md
    keep wiki regardless of acceptance
```

The held-out test set is not used for proposal acceptance.
