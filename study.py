from flask import Flask
from flask_restx import Api, Resource, fields

app = Flask(__name__)
api = Api(app, version='1.0', title='Test Api', description='A simple tutorial.')
ns = api.namespace('api', description='test api')

@api.route('/http/test')
class HttpTestApi(Resource):
    def get(self):
        return {'hello': 'word'}

@ns.route('/http/path/<string:tId>')
class HttpPathApi(Resource):
    def put(self, tId):
        return {'tId': tId}

@ns.route('/http/status')
class HttpStatus(Resource):
    def get(self):
        return {'msg': 'hello word'}, 301, {'ETag': 'v221018'}

# todo = api.model('Todo', {
#     'id': fields.Integer(readonly=True, description='id value'),
#     'name': fields.String(readonly=True, description='name value')
# })
#
# @ns.route('/todo')
# @ns.param('id', 'id value')
# class TodoApi(Resource):
#     @ns.doc('get task')
#     @ns.marshal_list_with(todo)
#     def get(self, id):
#         return [{'id': 1, 'name': 'task001'}]

if __name__ == '__main__':
    app.run(port=5000, debug=True)
