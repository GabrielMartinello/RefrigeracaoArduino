# import main Flask class and request object
from flask import Flask, request, jsonify, make_response
from flask_restful import Resource, Api
from json import dumps
from flask_cors import CORS, cross_origin
from model.temperatura import db, Temperatura, app, temperatura_schema, temperaturas_schema
from flask_marshmallow import Marshmallow

# create the Flask app

CORS(app)
api = Api(app)
ma = Marshmallow(app)

class Temperaturas(Resource):
    def get(self):
        all_temp = Temperatura.query.all()
        result = temperaturas_schema.dump(all_temp)
        return make_response(jsonify(result), 200) 

    def post(self):
        temp = Temperatura(temperatura=request.json['temperatura'], umidade=request.json['umidade'])
        db.session.add(temp)
        db.session.commit()
        result = temperatura_schema.dump(temp)
        return make_response(jsonify(result.data), 200)

    def put(self):
        temp = Temperatura.query.filter_by(id=request.json['id']).first()
        temp.temperatura = request.json['temperatura']
        temp.umidade = request.json['umidade']
        db.session.add(temp)
        db.session.commit()
        result = temperatura_schema.dump(temp)
        return make_response(jsonify(result), 200) 
    
class TemperaturaById(Resource):
    def delete(self, id):
        temp = Temperatura.query.filter_by(id=id).first()
        db.session.delete(temp)
        db.session.commit()
        return make_response(jsonify({"status": "success"}), 200) 

    def get(self, id):
        temp = Temperatura.query.filter_by(id=id).first()
        result = temperatura_schema.dump(temp)
        return make_response(jsonify(result), 200)     
    

api.add_resource(Temperaturas, '/temperatura') 
api.add_resource(TemperaturaById, '/temperaturas/<id>') 

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)