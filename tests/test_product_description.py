import unittest
from fastapi.testclient import TestClient
from app.api import app

class TestProductDesc(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_description_output(self):
        payload = {
            "product_name": "Erha Edge Node 500",
            "raw_features": ["Sub-10ms inference", "Local SQLite vector store", "Air-gapped security"],
            "category": "AI Hardware Node"
        }
        res = self.client.post("/generate-description", json=payload)
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertEqual(len(data["bullet_benefits"]), 3)
        self.assertIn("Erha Edge Node 500", data["short_pitch"])

if __name__ == "__main__":
    unittest.main()
