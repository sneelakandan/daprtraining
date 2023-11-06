from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/api/callServiceB')
def call_service_b():
    response = requests.get('http://localhost:3500/v1.0/invoke/serviceB/method/sayhello')
    return jsonify({"response": response.text})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=3000)

