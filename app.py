from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', defaults={'path': ''}, methods=['POST', 'PUT', 'GET', 'DELETE'])
@app.route('/<path:path>', methods=['POST', 'PUT', 'GET', 'DELETE'])
def handle_requests(path):
    response = {
        "error": "Too Many Requests",
        "status": 429
    }
    return jsonify(response), 429

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
