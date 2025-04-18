# REST API with Decision Rule

## Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

## Run with Docker

```bash
docker build -t modelML .
docker run -p 8000:8000 modelML
```

## Test the API

```bash
curl -X POST http://localhost:8000/predict -H "Content-Type: application/json" -d '{"age": 35, "income": 60000}'
```
