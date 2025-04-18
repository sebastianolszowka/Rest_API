import requests

def test_predict():
    url = "http://127.0.0.1:8000/predict"
    payload = {"age": 35, "income": 60000}
    response = requests.post(url, json=payload)
    assert response.status_code == 200
    assert response.json()["decision"] == "Approved"
