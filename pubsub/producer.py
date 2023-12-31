from flask import Flask, request
import requests
import os

app = Flask(__name__)

@app.route('/publish', methods=['POST'])
def publish_message():
    
    DAPR_HTTP_PORT = os.environ.get('DAPR_HTTP_PORT', '3500')
    content = request.json
    requests.post(f'http://localhost:{DAPR_HTTP_PORT}/v1.0/publish/neelsazuresb/neelstopic', json=content)
    return {}, 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
