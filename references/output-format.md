# Output format

Use Markdown by default. Preserve the user's requested format when specified.

## Decision header

- **Status:** `Hold` | `Proceed after listed conditions` | `No finance blocker identified`
- **Reviewer side:** payer/buyer, payee/seller, or other
- **Documents reviewed:** filenames, versions, and dates
- **Not reviewed / missing:** list
- **Jurisdiction and currency:** stated or `Needs confirmation`
- **Reliability:** readable/OCR-limited/incomplete

Use these evidence states consistently:

- `Missing`: verified absent from a complete reviewed document where the item should appear.
- `Not evidenced in materials reviewed`: the available summary, excerpt, OCR, or incomplete document set does not prove presence or absence.
- `Not applicable`: the check does not apply to this transaction.
- `Needs confirmation`: the fact or interpretation remains unresolved.

For prose summaries or emails, cite the source label and a short excerpt rather than inventing page or clause numbers. For OCR, label the locator `OCR-derived` and lower confidence when the text is uncertain.

## Executive summary

Use no more than five bullets: material economics, top blockers/high risks, unresolved approvals, and the recommended next step.

## Deal facts

| Field | Extracted value | Evidence | Confidence |
|---|---|---|---|
| Contract value |  | page/clause | High/Medium/Low |

Include at least parties, purpose, term, value, currency, tax basis, payment, invoice, delivery, acceptance, renewal, termination, and liability cap when relevant.

## Arithmetic and consistency checks

| Check | Inputs | Result | Status | Evidence |
|---|---|---|---|---|
| Milestones total | 30% + 60% + 10% | 100% | Pass | Schedule 2 |

Use `Pass`, `Fail`, or `Not testable`. Show the calculation for failures.

## Findings

| ID | Severity | Area | Finding and consequence | Evidence | Required action | Owner |
|---|---|---|---|---|---|---|

Evidence must include a locator and short quotation or state `Missing clause`. Required action should contain a preferred correction and, when appropriate, an acceptable fallback or compensating control.

## Questions and approvals

Separate factual questions from professional judgments. Name the required function and explain why its approval is needed.

If no approved playbook was supplied, include: `Policy comparison not performed; example materials are non-binding.`

## Post-signature obligation register

When decision status is `Hold`, title this section `Conditional draft obligations — not authorized` and do not mix remediation tasks with post-signature operating obligations.

| Obligation | Trigger | Due date / recurrence | Amount / formula | Owner | Evidence to retain | Source |
|---|---|---|---|---|---|---|

## Machine-readable findings

When automation or downstream import is requested, also return JSON with this minimal structure:

```json
{
  "decision_status": "Hold",
  "assumptions": [],
  "missing_documents": [],
  "findings": [
    {
      "id": "PAY-001",
      "severity": "high",
      "status": "deviation",
      "area": "payment",
      "title": "Advance payment lacks security",
      "contract_locator": "Section 4.1, page 6",
      "evidence_excerpt": "...",
      "financial_consequence": "...",
      "required_action": "...",
      "owner": "Treasury",
      "uncertainty": "..."
    }
  ],
  "obligations": []
}
```

Allowed severity values are `blocker`, `high`, `medium`, `low`, and `information`. Allowed comparison statuses are `complies`, `deviation`, `missing`, `conflict`, and `not_assessable`.
