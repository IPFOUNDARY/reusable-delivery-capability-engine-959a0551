# Test cases for the Reusable Delivery Capability Engine

import unittest
from src.core.engine import CapabilityEngine

class TestCapabilityEngine(unittest.TestCase):
    def setUp(self):
        self.engine = CapabilityEngine()

    def test_process_fnol(self):
        fnol_data = {'claim_id': '12345', 'incident_date': '2023-10-01'}
        response = self.engine.process_fnol(fnol_data)
        self.assertEqual(response['status'], 'success')

    def test_process_kyc(self):
        kyc_data = {'customer_id': '67890', 'name': 'John Doe'}
        response = self.engine.process_kyc(kyc_data)
        self.assertEqual(response['status'], 'success')

if __name__ == '__main__':
    unittest.main()
