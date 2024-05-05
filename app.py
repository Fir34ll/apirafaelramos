from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)  


df = pd.read_csv("Car_Insurance_Claim.csv")

@app.route('/calculate_credit_score', methods=['POST'])
def calculate_credit_score():
    data = request.json
 
    age = data['age']
    gender = data['gender']
    driving_experience = data['driving_experience']
    education = data['education']
    income = data['income']
    vehicle_year = data['vehicle_year']
    vehicle_type = data['vehicle_type']
    annual_mileage = data['annual_mileage']
    
   
    filtered_data = df[(df['AGE'] == age) &
                       (df['GENDER'] == gender) &
                       (df['DRIVING_EXPERIENCE'] == driving_experience) &
                       (df['EDUCATION'] == education) &
                       (df['INCOME'] == income) &
                       (df['VEHICLE_YEAR'] == vehicle_year) &
                       (df['VEHICLE_TYPE'] == vehicle_type)]
    
 
    credit_score = filtered_data['CREDIT_SCORE'].mean()
    
    
    if pd.isna(credit_score):
        return jsonify({'error': 'Não foi possível calcular o CREDIT_SCORE para os dados fornecidos'}), 400
    
    return jsonify({'credit_score': credit_score})

@app.route('/', methods=['GET'])
def index():
    return 'Bem-vindo à API de Seguro de Veículos'

if __name__ == '__main__':
    app.run(debug=True)
