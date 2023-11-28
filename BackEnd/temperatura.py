
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import date

app = Flask(__name__, template_folder='templates')
app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost:5432/Temperatura'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Temperatura(db.Model):
    # __tablename__ = "Temperatura"
    id = db.Column(db.Integer, primary_key=True)
    umidade = db.Column(db.Double, nullable=False)
    temperatura = db.Column(db.Double, nullable=False)
    data = db.Column(db.Date)

db.drop_all()
db.create_all()  

# Dados iniciais
temperatura = Temperatura(umidade='30.00', temperatura='25.00', data = date.today())
db.session.add(temperatura)
db.session.commit()

class TemperaturaSchema(ma.Schema):
    class Meta:
        fields = ("id", "umidade", "temperatura","temperaturamax", "temperaturamin", "data")

temperatura_schema = TemperaturaSchema()
temperaturas_schema = TemperaturaSchema(many=True)

@app.route('/temperatura/graphs')
def renderizeGraph():
    return render_template('index.html')