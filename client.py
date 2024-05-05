import requests

# URL da sua API
url = 'http://localhost:5000/calculate_credit_score'

# Dados para enviar na requisição POST
data = {
    'age': '16-25',
    'gender': 'male',
    'driving_experience': '0-9y',
    'education': 'high school',
    'income': 'poverty',
    'vehicle_year': 'before 2015',
    'vehicle_type': 'sedan',
    'annual_mileage': 12000
}

# Enviar requisição POST e obter resposta
response = requests.post(url, json=data)

# Exibir o resultado
print(response.json())
