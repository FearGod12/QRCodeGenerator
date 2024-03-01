import unittest
from app import app, SAMPLE_DATA

class TestApp(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello, world!')

    def test_create_qr_code(self):
        # Test with valid data
        data = SAMPLE_DATA
        response = self.client.post('/create_qr_code', json=data)
        self.assertEqual(response.status_code, 201)
        
        # Test with missing data
        data = {}
        response = self.client.post('/create_qr_code', json=data)
        self.assertEqual(response.status_code, 400)

    def test_fetch_qr_code(self):
        # Test with valid id
        response = self.client.get('/fetch_qr_code/1') 
        self.assertEqual(response.status_code, 200)
        
        # Test with invalid id
        response = self.client.get('/fetch_qr_code/999')
        self.assertEqual(response.status_code, 404)

    def test_fetch_user(self):
        # Test with valid id
        response = self.client.get('/fetch_user/1')
        self.assertEqual(response.status_code, 200)
        
        # Test with invalid id
        response = self.client.get('/fetch_user/999')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()