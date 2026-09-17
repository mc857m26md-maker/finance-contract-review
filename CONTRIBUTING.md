# Contributing

Thank you for helping improve finance contract review.

## Good contributions

- Finance-specific checks that prevent a concrete error or missed obligation.
- Better evidence, escalation, privacy, or authorization boundaries.
- Playbook schema improvements with backward-compatible examples.
- Deterministic checks with tests and no external dependency unless clearly justified.
- Translations that preserve the meaning of control and legal disclaimers.

Avoid jurisdiction-specific legal or tax rules in the core skill. Put such material in a clearly named optional reference, cite an authoritative source, state the jurisdiction and effective date, and explain how users should verify updates.

## Pull requests

1. Explain the failure mode or user need.
2. Keep the change narrowly scoped.
3. Run the skill validator and both helper scripts.
4. Include a synthetic example when behavior changes.
5. Confirm that no confidential or personal data is included.

Run the local checks from the repository root:

```bash
python skills/finance-contract-review/scripts/validate_playbook.py skills/finance-contract-review/assets/finance-playbook.example.json
python skills/finance-contract-review/scripts/verify_terms.py skills/finance-contract-review/assets/deal-terms.example.json
python -m unittest discover -s tests -v
```

When changing the skill, also run the Codex skill validator. When changing plugin metadata, run the plugin validator described in the OpenAI plugin-builder documentation.

Do not submit real contracts, private playbooks, customer names, personal data, credentials, or privileged legal material.

By participating, you agree to follow the [Code of Conduct](CODE_OF_CONDUCT.md).
