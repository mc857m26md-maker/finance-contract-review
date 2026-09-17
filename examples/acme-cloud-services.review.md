# Finance review — Synthetic Vendor Services Agreement

> **Decision status: Hold.** Do not route for signature or payment until the amount, milestone, acceptance, missing schedule, bank-change control, and renewal issues are resolved and the appropriate owners approve the revised terms.

This is a finance-control review of fictional test data, not legal or tax advice.

## Scope and assumptions

- Side reviewed: Buyer and payer.
- Materials reviewed: Main agreement only, draft dated 2026-09-01.
- Schedule A is referenced but not supplied.
- No approved company playbook or approval matrix was supplied. Policy comparison was not performed; example materials are non-binding.
- Currency assumed to be CNY because the agreement states CNY.

## Deal facts and reconciliation

| Item | Contract fact | Evidence | Check |
|---|---:|---|---|
| Fees excluding tax | CNY 100,000.00 | §2.1 | Stated |
| Tax | CNY 6,000.00 | §2.2 | Stated |
| Computed total | CNY 106,000.00 | §2.1 + §2.2 | Recalculated |
| Stated total | CNY 105,000.00 | §2.3 | **Mismatch: CNY 1,000.00** |
| Payment milestones | 30% + 80% | §3.1–3.2 | **Total: 110%** |
| Acceptance period | 3 calendar days | §4.2 | Deemed acceptance |
| Renewal | 12 months; 60-day notice | §5.1–5.2 | Auto-renewal |
| Renewal uplift | 15% | §5.3 | Automatic increase |

## Prioritized findings

| Priority | Finding and consequence | Evidence | Required pre-signature action | Owner / escalation |
|---|---|---|---|---|
| Critical | The price does not reconcile: 100,000 + 6,000 = 106,000, not 105,000. The ambiguity can produce incorrect PO, accrual, invoice, tax, or payment values. | §2.1–2.3 | Correct all amount fields and confirm whether fees or tax are wrong. Re-run reconciliation. | Commercial owner + Finance + Tax |
| Critical | Payment milestones total 110%, creating an explicit overpayment path. | §3.1–3.2 | Amend milestones to total exactly 100%; state the amount basis and corresponding invoice conditions. | Finance + Procurement |
| High | Schedule A is missing even though it defines deliverables and acceptance criteria. The review cannot verify what is purchased or when payment is earned. | §1; missing attachment | Obtain the final Schedule A, confirm version, and reconcile it to the agreement before signature. | Business owner + Procurement + Legal |
| High | Acceptance is deemed after three calendar days without objective tests. Payment may become due before the buyer establishes usable delivery. | §4.1–4.3 | Add measurable criteria, a practical review period, rejection/remediation steps, and written acceptance by an authorized owner. | Business owner + Finance + Legal |
| Critical | Bank details may be changed by email with no independent verification. This creates payment-redirection fraud risk. | §3.4 | Require independent callback to a previously verified contact, controlled vendor-master change, and dual approval. Do not rely on reply email alone. | Treasury/AP + Vendor master owner |
| High | Renewal is automatic, requires 60-day notice, and raises price by 15%. This can create unplanned spend and a missed exit window. | §5.1–5.3 | Prefer affirmative renewal or capped/index-linked pricing; otherwise record notice deadline, budget owner, and renewal decision owner. | Budget owner + Procurement |
| High | Supplier liability is limited to three months of paid fees while buyer payment obligations are unlimited. The financial exposure is asymmetric. | §6.1–6.2 | Quantify the cap under likely timing scenarios and route proposed language to Legal and the authorized commercial approver. | Legal + Business owner + Finance |

## Required approvals and open questions

1. What is the correct tax-inclusive contract value?
2. What payment schedule should replace the 110% total?
3. Where is the final Schedule A, and which version will be signed?
4. Who has authority to accept delivery and approve invoice release?
5. Does the buyer's approved vendor-master policy permit any bank-detail change by email?
6. What liability threshold requires CFO, controller, or legal escalation?

## Conditional obligation register

All items below are **Conditional — not authorized** while the decision status is `Hold`.

| Obligation | Trigger or due date | Owner | Evidence | Control |
|---|---|---|---|---|
| Advance payment | Five business days after signature | AP / Treasury | §3.1 | Block until corrected amount, valid invoice, approval, and verified bank master |
| Acceptance review | Within three calendar days after supplier email | Business owner | §4.1–4.2 | Replace with approved objective procedure before signature |
| Final payment | Five business days after acceptance | AP / Finance | §3.2 | Block until milestone percentage is corrected and acceptance evidence exists |
| Renewal decision | At least 60 days before term end | Budget owner / Procurement | §5.1–5.3 | Create reminder with sufficient internal review lead time |
| Renewal price review | Before each renewal | Finance / Procurement | §5.3 | Validate budget and approved price-adjustment position |

## Re-test conditions

Run the review again after receiving the complete Schedule A and a revised agreement. The new review should verify that the tax-inclusive total reconciles, milestones equal 100%, acceptance uses objective evidence, bank changes require independent verification, and renewal exposure is explicitly owned.
