# Agent Evals Lab (OpenClaw Skill)

<p align="left">
  <a href="https://github.com/vassiliylakhonin/Agent-Evals-Lab-For-ClawHub/stargazers"><img src="https://img.shields.io/github/stars/vassiliylakhonin/Agent-Evals-Lab-For-ClawHub?style=for-the-badge" alt="Stars"></a>
  <a href="https://github.com/vassiliylakhonin/Agent-Evals-Lab-For-ClawHub/network/members"><img src="https://img.shields.io/github/forks/vassiliylakhonin/Agent-Evals-Lab-For-ClawHub?style=for-the-badge" alt="Forks"></a>
  <a href="https://github.com/vassiliylakhonin/Agent-Evals-Lab-For-ClawHub/issues"><img src="https://img.shields.io/github/issues/vassiliylakhonin/Agent-Evals-Lab-For-ClawHub?style=for-the-badge" alt="Issues"></a>
  <a href="https://github.com/vassiliylakhonin/Agent-Evals-Lab-For-ClawHub/commits/main"><img src="https://img.shields.io/github/last-commit/vassiliylakhonin/Agent-Evals-Lab-For-ClawHub?style=for-the-badge" alt="Last Commit"></a>
  <a href="https://clawhub.ai/vassiliylakhonin/agent-evals-lab"><img src="https://img.shields.io/badge/ClawHub-install-blue?style=for-the-badge" alt="Install on ClawHub"></a>
  <a href="./LICENSE"><img src="https://img.shields.io/badge/license-MIT-green?style=for-the-badge" alt="License"></a>
</p>

Evaluate agent quality and reliability with practical scorecards:
- correctness, relevance, actionability,
- risk and safety flags,
- tool-call reliability,
- regression checks,
- prioritized fix plans.

---

## Why this skill

Most teams ship agent changes based on intuition.
This skill provides a repeatable evaluation loop with measurable outcomes and clear Go/No-Go guidance.

---

## Install

```bash
clawhub install agent-evals-lab
```

Install pinned version:

```bash
clawhub install agent-evals-lab --version 0.1.1
```

---

## Typical use

```text
Use $agent-evals-lab to audit this agent workflow, score quality dimensions, find top failure clusters, and propose prioritized fixes with regression checks.
```

---

## Output highlights

1. Executive Summary
2. Scorecard by dimension / task type / risk level
3. Failure Map with root-cause hypotheses
4. Top 5 prioritized fixes (impact vs effort)
5. 1-2 week regression plan
6. Go / Conditional Go / No-Go decision

---

## Repository structure

```text
skills/agent-evals-lab/
  SKILL.md
  references/eval-templates.md
```

---

## License

MIT
