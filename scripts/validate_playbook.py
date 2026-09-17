#!/usr/bin/env python3
"""Validate a finance-contract-review JSON playbook using only stdlib."""

import argparse
import json
import sys


SEVERITIES = {"blocker", "high", "medium", "low", "information"}
TOP_REQUIRED = {
    "schema_version": int,
    "name": str,
    "owner": str,
    "approved_by": list,
    "effective_date": str,
    "jurisdictions": list,
    "contract_types": list,
    "reviewer_sides": list,
    "rules": list,
}
RULE_REQUIRED = {
    "id": str,
    "area": str,
    "title": str,
    "severity": str,
    "applies_when": str,
    "preferred_position": str,
    "fallback_positions": list,
    "prohibited_positions": list,
    "escalate_to": list,
    "evidence_required": list,
}


def nonempty(value):
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, list):
        return len(value) > 0
    return value is not None


def validate(data):
    errors = []
    for key, expected_type in TOP_REQUIRED.items():
        if key not in data:
            errors.append("Missing top-level field: {}".format(key))
        elif not isinstance(data[key], expected_type):
            errors.append("{} must be {}".format(key, expected_type.__name__))

    if errors:
        return errors
    if data["schema_version"] != 1:
        errors.append("schema_version must be 1")
    for key in ("name", "owner", "approved_by", "effective_date", "jurisdictions", "contract_types", "reviewer_sides"):
        if not nonempty(data[key]):
            errors.append("{} must not be empty".format(key))

    ids = set()
    for index, rule in enumerate(data["rules"]):
        path = "rules[{}]".format(index)
        if not isinstance(rule, dict):
            errors.append("{} must be an object".format(path))
            continue
        for key, expected_type in RULE_REQUIRED.items():
            if key not in rule:
                errors.append("{}.{} is required".format(path, key))
            elif not isinstance(rule[key], expected_type):
                errors.append("{}.{} must be {}".format(path, key, expected_type.__name__))
        if any(key not in rule for key in RULE_REQUIRED):
            continue
        if rule["id"] in ids:
            errors.append("Duplicate rule id: {}".format(rule["id"]))
        ids.add(rule["id"])
        if rule["severity"] not in SEVERITIES:
            errors.append("{}.severity must be one of {}".format(path, sorted(SEVERITIES)))
        for key in ("id", "area", "title", "applies_when", "preferred_position"):
            if not nonempty(rule[key]):
                errors.append("{}.{} must not be empty".format(path, key))
        if not rule["escalate_to"]:
            errors.append("{}.escalate_to must name at least one owner".format(path))
        if not rule["evidence_required"]:
            errors.append("{}.evidence_required must name at least one item".format(path))
    if not data["rules"]:
        errors.append("rules must contain at least one rule")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("playbook", help="Path to a JSON playbook")
    args = parser.parse_args()
    try:
        with open(args.playbook, "r", encoding="utf-8") as handle:
            data = json.load(handle)
    except (OSError, ValueError) as exc:
        print("INVALID: {}".format(exc), file=sys.stderr)
        return 2
    errors = validate(data)
    if errors:
        print("INVALID")
        for error in errors:
            print("- {}".format(error))
        return 1
    print("VALID: {} rules".format(len(data["rules"])))
    return 0


if __name__ == "__main__":
    sys.exit(main())
