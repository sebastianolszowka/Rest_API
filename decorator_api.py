from flask import Flask, jsonify

app = Flask(__name__)

def round_result(func):
    def wrapper():
        result = func()
        result['value'] = round(result['value'], 2)
        return result
    return wrapper

@app.route('/')
@round_result
def example():
    return {"value": 3.141592}

if __name__ == '__main__':
    app.run()
