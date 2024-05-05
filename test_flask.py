import unittest
from app import app

class FlaskTest(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
    
    def test_index_endpoint(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Bem-vindo à API de Seguro de Veículos')
    
    def test_calculate_credit_score_endpoint(self):
        data = {
            'age': '65+',
            'gender': 'female',
            'driving_experience': '0-9y',
            'education': 'high school',
            'income': 'upper class',
            'vehicle_year': 'after 2015',
            'vehicle_type': 'sedan',
            'annual_mileage': 12000
        }
        response = self.app.post('/calculate_credit_score', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('credit_score', response.get_json())

if __name__ == '__main__':
    unittest.main()
