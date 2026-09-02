# Knowledge Access Control

## Default

| Component | raw | wiki | skills |
|---|---:|---:|---:|
| Inference Agent | own runtime only | No | Read |
| Wiki Maintainer | sampled read | Read/Write | Optional read |
| Skill Proposer | selected read | Read | Read |
| Gating Harness | validation traces | Append impact record | Candidate write/promote |

The separation is intentional.

Providing the persistent wiki directly to the inference agent during training can confound whether the executable skill itself captures the knowledge.
