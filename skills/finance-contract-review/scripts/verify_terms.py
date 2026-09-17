#!/usr/bin/env python3
"""Run deterministic arithmetic checks over extracted contract terms."""

import argparse
from decimal import Decimal, InvalidOperation
import json
import sys


def decimal(value, name):
    try:
        return Decimal(str(value))
    except (InvalidOperation, TypeError, ValueError):
        raise ValueError("{} is not a valid decimal".format(name))


def close(left, right, tolerance):
    return abs(left - right) <= tolerance


def check(data, tolerance):
    results = []
    amounts = data.get("amounts", {})
    if all(key in amounts for key in ("total_ex_tax", "tax", "total_inc_tax")):
        ex_tax = decimal(amounts["total_ex_tax"], "amounts.total_ex_tax")
        tax = decimal(amounts["tax"], "amounts.tax")
        inc_tax = decimal(amounts["total_inc_tax"], "amounts.total_inc_tax")
        actual = ex_tax + tax
        results.append({
            "check": "tax_total_reconciliation",
            "status": "pass" if close(actual, inc_tax, tolerance) else "fail",
            "expected": str(inc_tax),
            "actual": str(actual),
            "difference": str(actual - inc_tax),
        })

    lines = data.get("line_items", [])
    if lines and "total_ex_tax" in amounts:
        actual = sum((decimal(item["quantity"], "line_items.quantity") * decimal(item["unit_price"], "line_items.unit_price") for item in lines), Decimal("0"))
        expected = decimal(amounts["total_ex_tax"], "amounts.total_ex_tax")
        results.append({
            "check": "line_items_to_total_ex_tax",
            "status": "pass" if close(actual, expected, tolerance) else "fail",
            "expected": str(expected),
            "actual": str(actual),
            "difference": str(actual - expected),
        })

    milestones = data.get("milestones", [])
    if milestones:
        if all("percent" in item for item in milestones):
            actual = sum((decimal(item["percent"], "milestones.percent") for item in milestones), Decimal("0"))
            results.append({
                "check": "milestone_percent_total",
                "status": "pass" if close(actual, Decimal("100"), tolerance) else "fail",
                "expected": "100",
                "actual": str(actual),
                "difference": str(actual - Decimal("100")),
            })
        amount_basis = data.get("milestone_amount_basis")
        if amount_basis not in (None, "total_ex_tax", "total_inc_tax"):
            raise ValueError("milestone_amount_basis must be total_ex_tax or total_inc_tax")
        if all("amount" in item for item in milestones) and amount_basis is None:
            results.append({
                "check": "milestone_amount_total",
                "status": "not_testable",
                "reason": "milestone_amount_basis is not specified",
            })
        elif all("amount" in item for item in milestones) and amount_basis in amounts:
            actual = sum((decimal(item["amount"], "milestones.amount") for item in milestones), Decimal("0"))
            expected = decimal(amounts[amount_basis], "amounts.{}".format(amount_basis))
            results.append({
                "check": "milestone_amount_total",
                "status": "pass" if close(actual, expected, tolerance) else "fail",
                "basis": amount_basis,
                "expected": str(expected),
                "actual": str(actual),
                "difference": str(actual - expected),
            })
        elif all("amount" in item for item in milestones):
            results.append({
                "check": "milestone_amount_total",
                "status": "not_testable",
                "reason": "{} is missing from amounts".format(amount_basis),
            })
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("terms", help="JSON file with amounts, line_items, and/or milestones")
    parser.add_argument("--tolerance", default="0.01", help="Absolute decimal tolerance (default: 0.01)")
    args = parser.parse_args()
    try:
        with open(args.terms, "r", encoding="utf-8") as handle:
            data = json.load(handle)
        results = check(data, decimal(args.tolerance, "tolerance"))
    except (OSError, ValueError, KeyError) as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False))
        return 2
    print(json.dumps({"checks": results}, ensure_ascii=False, indent=2))
    return 1 if any(item["status"] == "fail" for item in results) else 0


if __name__ == "__main__":
    sys.exit(main())
