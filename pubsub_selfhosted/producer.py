from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/publish', methods=['POST'])
def publish_message():
    #include code for header section with dapr app id 
    
    content = request.json
    requests.post('http://localhost:3500/v1.0/publish/neelsazuresb/neelstopic', json=content)
    return {}, 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
