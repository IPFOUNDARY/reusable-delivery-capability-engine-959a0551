# Example usage of the Reusable Delivery Capability Engine

from src.core.engine import CapabilityEngine

# Initialize the engine
engine = CapabilityEngine()

# Example FNOL data
fnol_data = {
    'claim_id': '12345',
    'incident_date': '2023-10-01',
    'description': 'Car accident',
}

# Process FNOL
response = engine.process_fnol(fnol_data)
print(response)

# Example KYC data
kyc_data = {
    'customer_id': '67890',
    'name': 'John Doe',
    'address': '123 Main St',
}

# Process KYC
response = engine.process_kyc(kyc_data)
print(response)
