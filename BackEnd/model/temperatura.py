
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost:5432/Temperatura'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Temperatura(db.Model):
    # __tablename__ = "Temperatura"
    id = db.Column(db.Integer, primary_key=True)
    umidade = db.Column(db.String(120), nullable=False)
    temperatura = db.Column(db.String(120), unique=True, nullable=False)

db.drop_all()
db.create_all()  

# Dados iniciais
temperatura = Temperatura(umidade='30', temperatura='25 Graus')
db.session.add(temperatura)
db.session.commit()

class TemperaturaSchema(ma.Schema):
    class Meta:
        fields = ("id", "umidade", "temperatura")

temperatura_schema = TemperaturaSchema()
temperaturas_schema = TemperaturaSchema(many=True)        