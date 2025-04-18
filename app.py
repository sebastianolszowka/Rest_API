from flask import Flask, request, jsonify

app = Flask(__name__)

def decision_rule(age, income):
    if age > 30 and income > 50000:
        return "Approved"
    else:
        return "Rejected"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    if not data or 'age' not in data or 'income' not in data:
        return jsonify({'error': 'Missing age or income'}), 400

    try:
        age = int(data['age'])
        income = float(data['income'])
    except ValueError:
        return jsonify({'error': 'Invalid input type'}), 400

    decision = decision_rule(age, income)
    return jsonify({'decision': decision})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
