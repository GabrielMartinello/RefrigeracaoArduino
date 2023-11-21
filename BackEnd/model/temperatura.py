class Temperatura:
    def __init__(self, id, temperatura, umidade):
        self.id = id
        self.temperatura = temperatura
        self.umidade = umidade

    def to_dict(self):
        return {"id": self.id, "temperatura": self.temperatura, "umidade": self.umidade}