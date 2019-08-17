
from flask import Flask, request
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify

app = Flask(__name__)
api = Api(app)

CORS(app)

employees = {'employees': [{'id': 1, 'name': 'Emma'}, {'id': 2, 'name': 'Jane'}]}

@app.route("/")
def hello():
    return jsonify({'text': 'Hello world!'})

class Employees(Resource):
    def get(self):
        return employees['employees']

class Employees_Name(Resource):
    def get(self, employee_id):
        # result = {'data': {'id': 1, 'name': 'Emma'}}
        result = [emp for emp in employees['employees'] if emp['id'] == int(employee_id)]
        return jsonify(result)

api.add_resource(Employees, '/employees') # Route_1
api.add_resource(Employees_Name, '/employees/<employee_id>') # Route_3


if __name__ == '__main__':
    app.run(port=5002)