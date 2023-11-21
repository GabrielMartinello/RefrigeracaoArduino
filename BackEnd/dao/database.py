import os
import psycopg2
from dotenv import load_dotenv

#carrega os valores do .env
load_dotenv() 

class MyDatabase():
    def __init__(self, dbHost=os.environ.get('PG_HOST'),
                        dbPort=os.environ.get('PG_PORT'),
                        dbUser=os.environ.get('PG_USER'),
                        dbPassword=os.environ.get('PG_PASSWORD'),
                        db=os.environ.get('PG_DATABASE')):

        #Mostra as variáveis do banco que estão sendo passadas pelo .env
        print('HostName: ' + os.environ.get('PG_HOST'),
        ', Porta: ' + os.environ.get('PG_PORT'),
        ', Usuário banco: ' + os.environ.get('PG_USER'),
        ', Senha: ' + os.environ.get('PG_PASSWORD'),
        ', Nome do banco: ' + os.environ.get('PG_DATABASE'))

        self.conn = psycopg2.connect(host = dbHost, port = dbPort, user = dbUser, password = dbPassword, dbname = db)
        self.cur = self.conn.cursor()

    def getSelf(self):
        return self

    def query(self, query):
        self.cur.execute(query)
        return self.cur.fetchall()


    def close(self):
        self.cur.close()
        self.conn.close()   


                