import unittest
from app import create_app

class BasicTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_landing_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_auvo_route(self):
        response = self.client.get('/auvo_15')
        self.assertEqual(response.status_code, 200)

    def test_chatshub_route(self):
        response = self.client.get('/chatshub_16')
        self.assertEqual(response.status_code, 200)
