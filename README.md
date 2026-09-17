# Finance Contract Review

![Finance Contract Review](assets/social-preview.png)

[![Tests](https://github.com/mc857m26md-maker/finance-contract-review/actions/workflows/test.yml/badge.svg)](https://github.com/mc857m26md-maker/finance-contract-review/actions/workflows/test.yml)
[![Pages](https://github.com/mc857m26md-maker/finance-contract-review/actions/workflows/pages.yml/badge.svg)](https://github.com/mc857m26md-maker/finance-contract-review/actions/workflows/pages.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-0F172A.svg)](LICENSE)
[![Plugin](https://img.shields.io/badge/ChatGPT%20%2B%20Codex-Plugin-1E3A8A.svg)](.codex-plugin/plugin.json)

**Evidence before confidence.** Finance Contract Review is an open, bilingual agent skill and plugin for first-pass commercial contract review from a finance perspective.

It turns contract language into source-linked deal facts, deterministic arithmetic checks, prioritized findings, approval routes, and a post-signature obligation register. It is built for controllers, procurement finance, FP&A, accounts payable, shared services, and finance business partners.

[中文说明](README.zh-CN.md) · [Live site](https://mc857m26md-maker.github.io/finance-contract-review/) · [Worked example](examples/acme-cloud-services.review.md) · [Market landscape](docs/market-landscape.md)

## See it catch real finance problems

The included fictional vendor agreement contains five deliberate control failures:

| Finding | Evidence | Finance consequence |
|---|---|---|
| Contract total does not reconcile | 100,000 + 6,000 tax, but stated total is 105,000 | Incorrect PO, accrual, invoice, or payment |
| Payment milestones total 110% | 30% advance + 80% after acceptance | Overpayment exposure |
| Acceptance is deemed after three days | No objective acceptance criteria | Payment may trigger before usable delivery |
| Bank changes are accepted by email | No independent callback or dual control | Payment-diversion fraud risk |
| Renewal price rises 15% automatically | 60-day cancellation notice | Unplanned spend and missed exit window |

Read the [synthetic contract](examples/acme-cloud-services.synthetic.md) and its [evidence-linked review](examples/acme-cloud-services.review.md). No real contract data is included.

## Install

### Recommended: install the skill from GitHub

Ask Codex:

```text
Use $skill-installer to install
https://github.com/mc857m26md-maker/finance-contract-review/tree/main/skills/finance-contract-review
```

Start a new conversation after installation. Then attach a contract and say:

```text
Use $finance-contract-review to review this vendor agreement from the buyer and payer side.
Check amount and tax reconciliation, payment versus acceptance, renewal, bank-detail controls,
liability exposure, and post-signature obligations. Cite every material finding.
```

### Manual skill installation

```bash
git clone https://github.com/mc857m26md-maker/finance-contract-review.git
cp -R finance-contract-review/skills/finance-contract-review ~/.agents/skills/
```

The repository is also packaged as a skills-only plugin under [`.codex-plugin/plugin.json`](.codex-plugin/plugin.json) for catalog and workspace distribution.

## What it returns

1. `Hold`, `Proceed after listed conditions`, or `No finance blocker identified`.
2. Scope, assumptions, missing documents, and reliability limits.
3. Evidence-linked deal facts and cross-document checks.
4. Recomputed totals, taxes, milestones, currencies, and dates.
5. Prioritized findings with consequence, proposed control, owner, and escalation.
6. A post-signature obligation register with dates, formulas, and evidence.

`No finance blocker identified` is not legal approval, tax advice, authority to sign, or assurance that no risk exists.

## Deterministic checks

```bash
python skills/finance-contract-review/scripts/validate_playbook.py \
  skills/finance-contract-review/assets/finance-playbook.example.json

python skills/finance-contract-review/scripts/verify_terms.py \
  skills/finance-contract-review/assets/deal-terms.example.json

python -m unittest discover -s tests -v
```

The arithmetic helper checks only supplied structured values. It does not extract terms or make legal, tax, or accounting judgments. Exit code `1` means checks ran and found a reconciliation failure; exit code `2` means invalid input or runtime failure.

## Why this is different

- **Finance-first:** payment, invoice, tax, acceptance, rebates, renewal, authority, and cash exposure.
- **Evidence-linked:** every material conclusion points to a clause, page, heading, or exact excerpt.
- **Deterministic where possible:** arithmetic is recalculated rather than guessed.
- **Playbook-driven:** preferred, fallback, prohibited, and escalation positions stay distinct.
- **Lifecycle-minded:** accepted terms become owned post-signature tasks.
- **Human-accountable:** the skill routes decisions and never grants approval.

## Privacy and safety

This package does not operate a server or collect telemetry by itself. Confirm that the host product and connected tools are approved for the data involved. Never upload real contracts or confidential playbooks to public issues or pull requests. See [Privacy](PRIVACY.md), [Security](SECURITY.md), and [Terms](TERMS.md).

## Contribute

Finance practitioners are especially welcome. The most valuable contributions are synthetic contracts, reproducible missed checks, approved control patterns, and output examples.

- [Report a bug](https://github.com/mc857m26md-maker/finance-contract-review/issues/new?template=bug_report.yml)
- [Share privacy-safe usage feedback](https://github.com/mc857m26md-maker/finance-contract-review/issues/new?template=usage_feedback.yml)
- [Propose a feature](https://github.com/mc857m26md-maker/finance-contract-review/issues/new?template=feature_request.yml)
- Read [CONTRIBUTING.md](CONTRIBUTING.md) and the [roadmap](ROADMAP.md)

If the project saves you time or prevents a finance-control miss, consider starring it and sharing the worked example with another finance reviewer.

## License

[MIT](LICENSE)
