from dao.database import MyDatabase
from model.temperatura import Temperatura

db = MyDatabase()
dbInstance = db.getSelf()

def convertToDict(queryResult):

    # Converter os resultados para uma lista de objetos da classe Temperatura
    temperaturas_objetos = [Temperatura(id=result[0], temperatura=result[1], umidade=result[2]) for result in queryResult]

    # Converter os resultados para uma lista de dicionários
    temperaturas_dict = [temp.to_dict() for temp in temperaturas_objetos]

    # Retorna um dicionário
    return temperaturas_dict

class TemperaturaDAO:

    @staticmethod
    def findAllTemp():
        resultados = convertToDict(db.query("SELECT * FROM TEMPERATURA"))
        return resultados

