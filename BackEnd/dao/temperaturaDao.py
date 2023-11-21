from dao.database import MyDatabase
from model.temperatura import Temperatura
import json

db = MyDatabase()
dbInstance = db.getSelf()

def convertToJSON(queryResult):

    # Converter os resultados para uma lista de objetos da classe Temperatura
    temperaturas_objetos = [Temperatura(id=result[0], temperatura=result[1], umidade=result[2]) for result in queryResult]

    #Converte pra json string
    tempJson = json.dumps([temp.__dict__ for temp in temperaturas_objetos], indent=2)

    #retorna um json
    return json.loads(tempJson)

class TemperaturaDAO:

    @staticmethod
    def findAllTemp():
        resultados = convertToJSON(db.query("SELECT * FROM TEMPERATURA"))
        return resultados

