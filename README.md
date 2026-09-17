# Finance Contract Review Skill

An open, evidence-first Codex skill for reviewing commercial contracts from a finance perspective.

It turns a contract into a verifiable deal-facts table, arithmetic checks, prioritized findings, approval/escalation items, and a post-signature obligation register. It is designed for controllership, procurement finance, FP&A, shared services, and finance business partners—not as a substitute for legal, tax, treasury, accounting-policy, or authorized business approval.

[中文说明](README.zh-CN.md) · [Market landscape](docs/market-landscape.md) · [Example playbook](assets/finance-playbook.example.json)

## Why this skill exists

Most contract-review products are strong at clause discovery, playbook comparison, redlining, and workflow. Finance reviewers also need deterministic checks that are easy to overlook:

- amount, tax, line-item, milestone, and currency reconciliation;
- payment, invoice, delivery, and acceptance alignment;
- advances, deposits, rebates, credits, renewals, and minimum commitments;
- approval authority, counterparty and bank-detail controls;
- accounting-policy, tax, treasury, legal, and security escalation;
- post-signature obligations with owners, dates, formulas, and evidence.

This skill combines those needs in a tool-neutral workflow. Every material finding must point back to contract evidence or be labeled as not evidenced.

## Install

Clone the repository into your Codex skills directory:

```bash
git clone https://github.com/mc857m26md-maker/finance-contract-review.git ~/.codex/skills/finance-contract-review
```

Restart or refresh Codex skill discovery if needed. The skill supports normal automatic discovery and can also be invoked explicitly as `$finance-contract-review`.

## Use

Attach the contract and, when available, the SOW/order form, pricing schedule, amendments, approval memo, and company playbook.

Example prompt:

```text
Use $finance-contract-review to review this vendor agreement from the buyer/payer side.
Focus on amount and tax reconciliation, payment versus acceptance, auto-renewal,
liability exposure, and post-signature obligations. Cite page and clause for every finding.
```

The skill will ask a question only when a missing choice—most importantly which party you represent—would materially change the result. Otherwise it proceeds with labeled assumptions.

## What it returns

1. Decision status: `Hold`, `Proceed after listed conditions`, or `No finance blocker identified`.
2. Scope, assumptions, missing documents, and reliability limits.
3. Evidence-linked deal facts.
4. Arithmetic and cross-document consistency checks.
5. Prioritized findings with consequence, correction/fallback, owner, and escalation.
6. Questions and approvals for legal, tax, treasury, accounting policy, procurement, security, or an authorized approver.
7. A post-signature obligation register.

`No finance blocker identified` is not legal approval, tax advice, authority to sign, or assurance that no risk exists.

## Playbooks and deterministic checks

Copy `assets/finance-playbook.example.json`, replace the placeholders, and have the relevant control owners approve the rules before operational use.

Validate a playbook:

```bash
python scripts/validate_playbook.py assets/finance-playbook.example.json
```

Check extracted financial terms:

```bash
python scripts/verify_terms.py assets/deal-terms.example.json
```

The arithmetic helper checks only the structured values supplied to it. It does not extract terms from documents or make legal, tax, or accounting judgments.
Its JSON fields and exit codes are documented in [references/structured-terms-schema.md](references/structured-terms-schema.md). In particular, exit code `1` means checks ran successfully and found a reconciliation failure; exit code `2` means invalid input or a runtime error.

Run the unit tests:

```bash
python -m unittest discover -s tests -v
```

## Design principles

- **Evidence before confidence:** findings include stable contract locators and minimal source excerpts.
- **Role-aware:** payer and payee risk can be opposite under the same wording.
- **Playbook-driven:** preferred, fallback, prohibited, and escalation positions remain distinct.
- **Deterministic where possible:** calculations are recomputed, not guessed by a language model.
- **Human accountability:** the skill routes decisions to named owners and never grants approval.
- **Lifecycle-minded:** accepted terms become post-signature tasks, not forgotten prose.
- **Privacy-conscious:** contract text is not sent to an external service without authorization.

## Repository contents

```text
finance-contract-review/
├── SKILL.md
├── agents/openai.yaml
├── assets/
│   ├── deal-terms.example.json
│   ├── finance-playbook.example.json
│   └── review-report-template.md
├── docs/market-landscape.md
├── references/
│   ├── finance-review-checklist.md
│   ├── output-format.md
│   ├── risk-and-escalation.md
│   └── structured-terms-schema.md
└── scripts/
    ├── validate_playbook.py
    └── verify_terms.py
```

## Contributing and security

Contributions are welcome; see [CONTRIBUTING.md](CONTRIBUTING.md). Do not put real contracts, personal data, credentials, privileged material, or confidential company playbooks in issues or pull requests. Report security concerns as described in [SECURITY.md](SECURITY.md).

## License

[MIT](LICENSE). This project provides a review workflow and templates, not legal, tax, accounting, or investment advice.

