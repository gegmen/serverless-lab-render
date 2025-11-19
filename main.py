from flask import Flask, request, jsonify

app = Flask(__name__)

# Существующий endpoint для GET /
@app.route('/')
def hello():
    return 'Hello, World!'

# Добавьте этот новый endpoint для POST /echo
@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json()
    if data:
        # Возвращаем полученные данные обратно
        return jsonify({
            "status": "success",
            "received": data
        })
    else:
        return jsonify({"error": "No JSON data received"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)