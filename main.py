from flask import Flask, request
from flask_restx import Api, Resource, fields

import algo01.add as algo01
import algo02.min as algo02

app = Flask(__name__)
api = Api(app, version='1.0', title='Algorithm Api Document', description='Python REST API Demo')
ns01 = api.namespace('ns01', description='algo01 group')
ns02 = api.namespace('ns02', description='algo02 group')

@ns01.route('/algo01/add')
@ns01.param('m', 'number m')
@ns01.param('n', 'number n')
class Algo01AddApi(Resource):
    @ns01.doc('algo01 add')
    def get(self):
        result = algo01.add(request.args.get('m', default=0, type=int), request.args.get('n', default=0, type=int))
        return {'result': result}

@ns02.route('/algo02/min')
@ns02.param('m', 'number m')
@ns02.param('n', 'number n')
class Algo02AddApi(Resource):
    @ns02.doc('algo01 add')
    def get(self):
        result = algo02.min(request.args.get('m', default=0, type=int), request.args.get('n', default=0, type=int))
        return {'result': result}

if __name__ == '__main__':
    app.run(port=5000, debug=True)
