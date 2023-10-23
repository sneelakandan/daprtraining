from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/dapr/subscribe', methods=['GET'])
def subscribe():
    subscriptions = [{'pubsubname': 'neelsazuresb', 'topic': 'neelstopic', 'route': 'neelstopic'}]
    return json.dumps(subscriptions)

'''
@app.route('/neelstopic', methods=['POST'])
def new_order():
    print(request.json)
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 
    
'''

@app.route('/neelstopic', methods=['POST'])
def neelstopic_subscriber():
    print(f'A: {request.json}', flush=True)
 #   print('Received message "{}" on topic "{}"'.format(request.json['data']['message'], request.json['topic']), flush=True)
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

if __name__ == "__main__":
    app.run(port=3000)