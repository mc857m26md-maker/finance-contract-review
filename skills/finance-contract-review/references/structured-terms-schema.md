# Structured terms for deterministic checks

`scripts/verify_terms.py` accepts a UTF-8 JSON object. Use decimal strings rather than binary floating-point numbers when possible.

```json
{
  "currency": "CNY",
  "amounts": {
    "total_ex_tax": "100000.00",
    "tax": "6000.00",
    "total_inc_tax": "106000.00"
  },
  "line_items": [
    {"description": "Service", "quantity": "10", "unit_price": "10000.00"}
  ],
  "milestone_amount_basis": "total_inc_tax",
  "milestones": [
    {"name": "Advance", "percent": "30", "amount": "31800.00"},
    {"name": "Acceptance", "percent": "70", "amount": "74200.00"}
  ]
}
```

Supported checks:

- `total_ex_tax + tax = total_inc_tax`;
- sum of `quantity × unit_price = total_ex_tax`;
- milestone percentages sum to 100;
- milestone amounts sum to the field named by `milestone_amount_basis`.

Allowed milestone bases are `total_ex_tax` and `total_inc_tax`. If the contract does not make the basis clear, do not guess: omit `milestone_amount_basis`, show calculations against both plausible bases in the narrative report, and mark the basis `Needs confirmation`. The script will then report the amount-total check as not testable.

Exit codes:

- `0`: checks completed and none failed;
- `1`: checks completed and at least one failed;
- `2`: invalid input or runtime error.

Exit code `1` means the checker successfully found a reconciliation failure; it is not a script crash.
