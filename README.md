# REST API – Decyzja kredytowa na podstawie wieku i dochodu

Sebastian Olszówka
Analiza danych w czasie rzeczywistym

## Opis projektu

Prosta aplikacja REST API stworzona z użyciem frameworka Flask, służąca do podejmowania decyzji kredytowej na podstawie wieku i dochodu.  
W aplikacji zaimplementowano:

- API z obsługą żądań POST
- Regułę decyzyjną
- Standaryzację danych
- Testy jednostkowe
- Obsługę błędów
- Możliwość uruchomienia z Docker

## Uruchomienie lokalnie

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

## Uruchomienie z użyciem Docker

```bash
docker build -t modelML .
docker run -p 8000:8000 modelML
```

## Testowanie API (przykład zapytania)

```bash
curl -X POST http://localhost:8000/predict \
     -H "Content-Type: application/json" \
     -d '{"age": 35, "income": 60000}'
```

Odpowiedź:
```json
{
  "age_standardized": 0.36,
  "income_standardized": 0.6,
  "decision": "Approved"
}
```

## Struktura plików

- app.py – główna aplikacja Flask
- requirements.txt – lista zależności
- test_app.py – test jednostkowy
- Dockerfile – konfiguracja kontenera
- basic_api.py, error_handling_api.py, decorator_api.py – wcześniejsze wersje API

## Autor

Sebastian Olszówka  
so140897@student.sgh.waw.pl 
https://github.com/sebastianolszowka
