import requests

# URL da sua API
url = 'http://localhost:5000/calculate_credit_score'

# Dados para enviar na requisição POST
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

# Enviar requisição POST e obter resposta
response = requests.post(url, json=data)

# Verificar o código de status da resposta
if response.status_code == 200:
    print("CREDIT_SCORE calculado com sucesso:")
    print("CREDIT_SCORE:", response.json()['credit_score'])
else:
    print("Erro ao calcular o CREDIT_SCORE:", response.text)
