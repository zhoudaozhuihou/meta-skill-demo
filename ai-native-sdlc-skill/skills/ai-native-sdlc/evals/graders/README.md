# Grader Guidance

Prefer deterministic graders for observable outcomes:

- file exists / does not exist;
- command exit code;
- tests pass;
- forbidden path unchanged;
- schema validation;
- expected endpoint/status behavior.

Use LLM-assisted grading only for semantics that cannot be reliably expressed as deterministic assertions, such as plan completeness or whether a review finding is well-supported.

For high-risk evals, deterministic safety assertions should be mandatory even when semantic graders are used.
