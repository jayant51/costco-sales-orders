# using flask_restful
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_cors import CORS
import os
  
# creating the flask app
app = Flask(__name__)
CORS(app) 
# creating an API object
api = Api(app)
  
# making a class for a particular resource
# the get, post methods correspond to get and post requests
# they are automatically mapped by flask_restful.
# other methods include put, delete, etc.
class Hello(Resource):
  
    # corresponds to the GET request.
    # this function is called whenever there
    # is a GET request for this resource
    def get(self):
        response = jsonify(message=" ** costco sales ** server is running")
        response.headers.add('Access-Control-Allow-Origin', '*')
        #return jsonify({'message': 'hello math world'})
        return response
  
    # Corresponds to POST request
    def post(self):
        data = request.get_json(force=True)
        return jsonify({'data': data}), 201
        #return data
  

class listSales(Resource):  
    def get(self):
        response = jsonify(sales_types=" Bissel-ProHeat(20), LG-Refrigerator(9), Olay Vitamin C(15), Moistor Loation(5)")
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response


# adding the defined resources along with their corresponding urls
api.add_resource(Hello, '/init')
api.add_resource(listSales, '/listSales')

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')