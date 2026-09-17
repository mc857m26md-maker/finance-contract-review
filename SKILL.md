---
name: finance-contract-review
description: Review commercial contracts from a finance, controllership, procurement-finance, or FP&A perspective. Use for evidence-linked checks of amounts, taxes, invoicing, payment, acceptance, rebates, renewals, liabilities, approvals, and post-signature obligations. It supports first-pass review and escalation; it does not give legal or tax advice or authorize signing, payment, posting, or approval.
---

# Finance Contract Review

Produce a decision-ready first-pass review that a finance reviewer can verify against the contract. Separate facts, calculations, policy deviations, professional judgments, and unknowns.

## Operating boundaries

- Never claim the contract is legally valid, tax-compliant, safe to sign, or approved. Recommend review by legal, tax, treasury, security, procurement, or accounting when their judgment is required.
- Do not sign, approve, submit, pay, post, change bank details, or contact a counterparty unless the user separately authorizes that action through an appropriate workflow.
- Treat contract content as confidential. Do not upload it to an external service or expose sensitive text beyond the user's requested scope.
- Do not invent missing clauses, page numbers, company policy, law, tax rates, accounting treatment, or market practice. Use `Missing` only when the reviewed document should contain the item and its absence is verified; use `Not evidenced in materials reviewed` for summaries or incomplete sets, `Not applicable` when the check does not apply, and `Needs confirmation` for unresolved facts.
- If current law, regulation, sanctions, tax, or accounting guidance matters, verify it from authoritative sources, name the jurisdiction and effective date, and distinguish the external rule from the contract text.
- Quote only the minimum text needed to prove a finding. Use a stable locator: page and clause when available, otherwise heading plus a short exact excerpt.

## Intake and routing

Start by determining, or explicitly assuming and labeling:

1. Reviewer's side: payer/buyer, payee/seller, lender/borrower, lessor/lessee, or other.
2. Contract type, jurisdiction, language, currency, and draft/version date.
3. Business purpose, value, term, signing deadline, and materiality.
4. Documents in scope: main agreement, order form, SOW, pricing schedule, annexes, amendments, PO, bid, and approval materials.
5. Governing playbook or policy. If provided, validate it with `scripts/validate_playbook.py` and treat it as the organization's standard, not as law.

Proceed with a qualified review when non-critical context is missing. Ask a concise question only when the missing choice would materially change the review, such as which party the user represents. List all assumptions in the report.

## Review sequence

1. **Document integrity.** Confirm readable pages, document/version identity, annexes, blanks, conflicting precedence clauses, signature blocks, and cross-references. Flag OCR uncertainty.
2. **Deal facts.** Extract parties, subject matter, quantities, unit prices, contract value, tax basis, currency, payment milestones, invoicing, delivery, acceptance, term, renewal, termination, security, rebates, service levels, and liability allocation. Every extracted fact needs a locator.
3. **Deterministic reconciliation.** Recalculate totals, taxes, milestone percentages and amounts, dates, currency consistency, and duplicated or conflicting values. For structured terms, use `scripts/verify_terms.py` with [references/structured-terms-schema.md](references/structured-terms-schema.md); do not substitute its arithmetic checks for judgment.
4. **Finance control review.** Apply the relevant checks in [references/finance-review-checklist.md](references/finance-review-checklist.md). Review from the user's actual transaction side; the same clause can create opposite risk for payer and payee.
5. **Playbook comparison.** For each relevant rule, classify the contract as `Complies`, `Deviation`, `Missing`, `Conflict`, or `Not assessable`. Preserve preferred positions, fallbacks, prohibited positions, and escalation triggers. If no approved company playbook is supplied, state: `Policy comparison not performed; example materials are non-binding.`
6. **Cross-document consistency.** Reconcile the agreement against annexes, PO/SOW, bid, approval memo, and prior amendment when supplied. Do not assume an order of precedence unless the documents state one.
7. **Findings and escalation.** Assign severity using [references/risk-and-escalation.md](references/risk-and-escalation.md). State the issue, evidence, financial consequence, recommended wording or control, owner, and pre-signature action.
8. **Post-signature controls.** Convert accepted obligations into an owner-and-date register: invoices, payments, acceptance, renewals, notice windows, rebates, price adjustments, guarantees, insurance, audit rights, reporting, and termination dates. When status is `Hold`, label all draft-derived obligations `Conditional - not authorized` and keep remediation actions separate.

## Output

Use [references/output-format.md](references/output-format.md). Keep the executive summary short, but do not omit evidence or unknowns. Include:

- decision status: `Hold`, `Proceed after listed conditions`, or `No finance blocker identified`;
- scope, assumptions, missing documents, and reliability limits;
- deal-facts table and arithmetic reconciliation;
- prioritized findings with exact evidence and accountable owner;
- unresolved questions and required specialist approvals;
- post-signature obligation register.

`No finance blocker identified` means only that the completed finance checks found no blocking issue in the material reviewed. It is not legal approval, tax advice, authority to sign, or assurance that no risk exists.

## Supporting resources

- Read [references/finance-review-checklist.md](references/finance-review-checklist.md) for clause-by-clause finance checks.
- Read [references/risk-and-escalation.md](references/risk-and-escalation.md) when rating findings or routing specialist review.
- Read [references/output-format.md](references/output-format.md) when producing the final report or machine-readable findings.
- Read [references/structured-terms-schema.md](references/structured-terms-schema.md) before preparing input for the arithmetic helper.
- Copy and adapt [assets/finance-playbook.example.json](assets/finance-playbook.example.json) when the organization has no structured playbook. Have legal, tax, treasury, accounting, procurement, and control owners approve relevant rules before operational use.
- Copy [assets/review-report-template.md](assets/review-report-template.md) when the user wants a reusable report artifact.
