from flask import Flask, request
# from flask_restx import Api, Resource, fields

import algo01.add as algo01
import algo02.min as algo02

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello word'

@app.route('/hello/<name>')
def helloName(name):
    return 'hello ' + name

@app.route('/json', methods=['POST'])
def add():
    print(request.headers)
    return request.json['m'] + request.json['n']

@app.route('/algo01/add')
def algo01Add():
    return str(algo01.add(request.args.get('m', default=0, type=int), request.args.get('n', default=0, type=int)))

@app.route('/algo02/min')
def algo02Min():
    return str(algo02.min(request.args.get('m', default=0, type=int), request.args.get('n', default=0, type=int)))

if __name__ == '__main__':
    app.run(port=5000, debug=True)
