# Trace Sampling

The paper's reported implementation samples up to eight training traces per iteration:

- up to 5 failing traces for root-cause analysis;
- up to 3 passing traces for successful-strategy extraction.

It caps each execution log at 15,000 characters before prompt injection.

For production systems, treat these as useful defaults rather than universal constants.

Recommended sampling priority:

1. new failure modes;
2. recurring failures;
3. high-severity failures;
4. surprising successes;
5. representative normal successes.

Keep the complete immutable trace in `raw/`; truncation should occur only in the context presented to an analysis agent.
