# Inference Agent Contract

The inference agent is the task executor being improved.

During WikiSkill training rollouts it receives:

- task context;
- tools;
- active executable skills.

It should normally not receive the persistent Wiki.

The outer harness records observable trajectory data and evaluation outcomes into the Raw Layer.

The inference agent must not mutate the WikiSkill knowledge base directly.
