from flask import Flask

app = Flask(__name__)

@app.route('/sayhello')
def sayhello():
    return 'Hello from Service B!'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=4000)
