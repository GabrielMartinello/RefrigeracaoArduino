from flask import Flask, request, jsonify, make_response
from flask_restful import Resource, Api
from flask_cors import CORS
from temperatura import db, Temperatura, app, temperatura_schema, temperaturas_schema
from flask_marshmallow import Marshmallow
from datetime import date
from sqlalchemy import text

CORS(app)
api = Api(app)
ma = Marshmallow(app)

class TemperaturasAvg(Resource):
   def get(self):
        with db.engine.connect() as con:
            query = "SELECT T.DATA, AVG(T.TEMPERATURA) AS TEMPERATURA, MAX(temperatura) AS TEMPERATURAMAX, MIN(temperatura) AS TEMPERATURAMIN FROM TEMPERATURA T GROUP BY T.DATA"
            temps = con.execute(text(query))
            result = temperaturas_schema.dump(temps)
            return make_response(jsonify(result), 200) 

class Temperaturas(Resource):
    def get(self):
        all_temp = Temperatura.query.all()
        result = temperaturas_schema.dump(all_temp)
        return make_response(jsonify(result), 200) 

    def post(self):
        temp = Temperatura(temperatura=request.json['temperatura'], umidade=request.json['umidade'], data=date.today())
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

api.add_resource(TemperaturasAvg, '/temperatura/avg') 
api.add_resource(Temperaturas, '/temperatura') 
api.add_resource(TemperaturaById, '/temperaturas/<id>') 

# app.run(debug=False, port=8090)
if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')