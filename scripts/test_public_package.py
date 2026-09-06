"""Public-package tests without private paper/answer fixtures."""
import unittest
from copy import deepcopy
from preflight import audit
from validate_paper import ROOT,read_json,check_state,local_asset,schema_errors

class PublicPackageTests(unittest.TestCase):
    def test_package(self):self.assertEqual(audit()['errors'],[])
    def test_blank_starter(self):
        d=read_json(ROOT/'state/STARTER_STATE.json')
        self.assertEqual(d['history'],[]);self.assertEqual(d['next_paper'],1)
    def test_invalid_state_rejected(self):
        d=deepcopy(read_json(ROOT/'state/STARTER_STATE.json'));d['next_paper']=0
        self.assertTrue(check_state(d))
    def test_missing_paper_rejected(self):
        s=read_json(ROOT/'PAPER_SCHEMA.json');self.assertTrue(schema_errors({},s,s))
    def test_asset_escape_rejected(self):
        with self.assertRaises(ValueError):local_asset(ROOT,'../outside.png')
    def test_no_private_fixtures(self):
        for name in ['examples','state/OWNER_SERIES_STATE.json','state/CURRENT_STATE.json','references/historical-ecology.md','references/mock-01-04-ecology.md']:
            self.assertFalse((ROOT/name).exists(),name)

if __name__=='__main__':unittest.main()
