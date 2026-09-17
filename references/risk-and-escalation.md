# Risk and escalation

Rate the finding, not the whole contract. Use impact, likelihood, detectability, and reversibility as judgment factors; do not imply false numerical precision.

| Severity | Use when | Default action |
|---|---|---|
| Blocker | Signing would exceed authority, payment details are unverified, a material amount cannot be reconciled, a material referenced document defining scope, price, acceptance, or another essential term is missing, a prohibited playbook position is present, or a credible fraud/compliance concern exists | Hold and route to the named control owner before signing |
| High | Material cash, tax, accounting, liability, credit, renewal, or enforceability exposure could occur and ordinary downstream controls may not prevent it | Resolve, obtain explicit exception approval, or document an accepted fallback before signing |
| Medium | The term is non-standard or operationally weak but exposure is bounded or recoverable | Negotiate or add a compensating control and owner |
| Low | Drafting, clarity, or administration issue with limited financial effect | Clean up when practical and record if accepted |
| Information | Fact, dependency, or observation without a current adverse conclusion | Track if useful; do not inflate risk counts |

## Mandatory specialist routing

- **Legal:** enforceability, governing law, liability/indemnity interpretation, unusual termination, IP, competition, employment, privacy, sanctions, disputes, or regulatory obligations.
- **Tax:** tax rate/treatment, withholding, permanent establishment, transfer pricing, customs, cross-border supply, gross-up, invoice compliance, or tax-change allocation.
- **Accounting policy:** revenue or lease classification, capitalization, variable consideration, principal-agent, embedded financing/derivatives, impairment, provisions, or disclosure.
- **Treasury:** FX exposure, hedging, guarantees, letters of credit, cash pooling, unusual payment rails, financing terms, or bank-detail changes.
- **Procurement/vendor risk:** supplier due diligence, concentration, solvency, subcontracting, continuity, insurance, or sourcing-policy deviation.
- **Security/privacy:** personal or sensitive data, security commitments, incident timing, data residency, subprocessors, or audit evidence.
- **Authorized approver:** any policy exception, material commitment, advance payment, minimum commitment, unlimited exposure, or non-standard approval threshold.

## Finding construction

Each finding must answer:

1. What does the contract say or omit?
2. Where is the evidence?
3. Why does it matter financially or operationally?
4. Which playbook/policy rule applies, if any?
5. What is the preferred correction and acceptable fallback?
6. Who must decide, and by when?
7. What remains uncertain?

Never lower a rating merely because a reviewer can monitor the issue after signing when the exposure should be resolved before signing.

## Bank-detail severity examples

- A clause that permits email-only bank changes is normally **High** because it creates a weak control design.
- A pending bank-change request that has not completed independent verification is a **Blocker** for master-data change and payment.
- An actual instruction to pay an unverified account is a **Blocker** and should be routed immediately to Treasury/AP and the fraud-response process.
