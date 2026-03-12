# Eval Templates

## Minimal Test Case Schema

```yaml
id: TC-001
task_type: qa|automation|planning|triage
risk_level: low|medium|high
input: "user request"
expected: "what good looks like"
must_not: "critical failure to avoid"
```

## Scoring Rubric (1-5)

- 5: excellent, no material issues
- 4: good, minor issues only
- 3: acceptable, notable weaknesses
- 2: poor, likely user friction/risk
- 1: failed, unacceptable

## Failure Cluster Tags

- factual_error
- weak_reasoning
- tool_misuse
- tool_failure_recovery
- unsafe_or_irreversible_advice
- missing_clarification
- over_clarification
- non_actionable_output

## Priority Matrix

Impact × Effort:
- High impact + Low effort = Do now
- High impact + Medium effort = Next sprint
- Low impact + High effort = Backlog
