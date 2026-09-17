import copy
from decimal import Decimal
import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, str(path))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


validate_playbook = load_module("validate_playbook", ROOT / "scripts" / "validate_playbook.py")
verify_terms = load_module("verify_terms", ROOT / "scripts" / "verify_terms.py")


class ValidatePlaybookTests(unittest.TestCase):
    def setUp(self):
        with (ROOT / "assets" / "finance-playbook.example.json").open(encoding="utf-8") as handle:
            self.playbook = json.load(handle)

    def test_example_is_valid(self):
        self.assertEqual([], validate_playbook.validate(self.playbook))

    def test_duplicate_rule_id_is_rejected(self):
        duplicate = copy.deepcopy(self.playbook["rules"][0])
        self.playbook["rules"].append(duplicate)
        errors = validate_playbook.validate(self.playbook)
        self.assertTrue(any("Duplicate rule id" in error for error in errors))

    def test_invalid_severity_is_rejected(self):
        self.playbook["rules"][0]["severity"] = "urgent"
        errors = validate_playbook.validate(self.playbook)
        self.assertTrue(any("severity" in error for error in errors))


class VerifyTermsTests(unittest.TestCase):
    def setUp(self):
        with (ROOT / "assets" / "deal-terms.example.json").open(encoding="utf-8") as handle:
            self.terms = json.load(handle)

    def test_example_passes_all_checks(self):
        results = verify_terms.check(self.terms, Decimal("0.01"))
        self.assertTrue(results)
        self.assertTrue(all(item["status"] == "pass" for item in results))

    def test_bad_total_fails(self):
        self.terms["amounts"]["total_inc_tax"] = "105000.00"
        results = verify_terms.check(self.terms, Decimal("0.01"))
        failed = [item for item in results if item["status"] == "fail"]
        self.assertTrue(any(item["check"] == "tax_total_reconciliation" for item in failed))

    def test_bad_milestone_percent_fails(self):
        self.terms["milestones"][1]["percent"] = "60"
        results = verify_terms.check(self.terms, Decimal("0.01"))
        failed = [item for item in results if item["status"] == "fail"]
        self.assertTrue(any(item["check"] == "milestone_percent_total" for item in failed))

    def test_missing_milestone_basis_is_not_testable(self):
        del self.terms["milestone_amount_basis"]
        results = verify_terms.check(self.terms, Decimal("0.01"))
        self.assertTrue(any(item["check"] == "milestone_amount_total" and item["status"] == "not_testable" for item in results))

    def test_ex_tax_milestone_basis(self):
        self.terms["milestone_amount_basis"] = "total_ex_tax"
        self.terms["milestones"][0]["amount"] = "30000.00"
        self.terms["milestones"][1]["amount"] = "70000.00"
        results = verify_terms.check(self.terms, Decimal("0.01"))
        amount_check = [item for item in results if item["check"] == "milestone_amount_total"][0]
        self.assertEqual("pass", amount_check["status"])
        self.assertEqual("total_ex_tax", amount_check["basis"])


if __name__ == "__main__":
    unittest.main()
