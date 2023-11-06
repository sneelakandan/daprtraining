# serviceA.py
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/set', methods=['POST'])
def set_key_value():
    app_id = 'my-python-app'

    key = request.json['key']
    value = request.json['value']

    headers = {
        'Content-Type': 'application/json',
        'dapr-app-id': app_id,
    }

    url = f'http://127.0.0.1:3500/v1.0/state/statestore'  # Use statestore as the store name
    data = [{'key': key, 'value': value}]

    response = requests.post(url, headers=headers, json=data)
    return jsonify({'message': 'Key-Value Pair Set'})

@app.route('/get/<key>', methods=['GET'])
def get_value(key):


    url = f'http://127.0.0.1:3500/v1.0/state/statestore/{key}'  # Use statestore as the store name
    response = requests.get(url)
    
    
    if response.status_code == 200:
        try:
            print('Dapr response is ', response.status_code, response.text)
            value = response.json()
            return jsonify({'key': key, 'value': value})
           
        except (IndexError, KeyError):
            print("value of key received is ", key)
            return jsonify({'message': 'Invalid response format from Dapr.'}, 500)
    else:
        return jsonify({'message': f'Key "{key}" not found in the state store.'}, 404)

if __name__ == '__main__':
    app.run(port=3000)
