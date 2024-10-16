import psycopg2
from dotenv import load_dotenv
import os

class DataBaseMeta(type):

    __instances = None

    def __call__(cls, *args, **kwargs):
        if cls.__instances is None:
            instance = super().__call__(*args, **kwargs)
            cls.__instances = instance
        return cls.__instances


class Database(metaclass=DataBaseMeta):
    
    def __init__(self):
        try:
            load_dotenv('/POO-PRACTICA/TRABAJO_PRACTICO_N5/Ejercicio_4/.env')
            self.conexion = psycopg2.connect(HOST=os.getenv('host'), PORT=os.getenv('port'), BASE=os.getenv('base'), USER=os.getenv('user'), PASSW=os.getenv('passw'))
            print('Conexion exitosa')
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
    

    def getAll(self, query):
        cursor = self.conexion.cursor()
        cursor.execute(query)
        return cursor.fetchall()
    
    
    def get(self, query):
        cursor = self.conexion.cursor()
        cursor.execute(query)
        return cursor.fetchone()

    def query(self, query):
        cursor = self.conexion.cursor()
        result = cursor.execute(query)
        cursor.connection.commit()
        return result