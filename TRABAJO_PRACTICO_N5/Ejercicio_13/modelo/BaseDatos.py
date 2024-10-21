import psycopg2
from psycopg2 import OperationalError
import threading
from datetime import datetime
from dotenv import load_dotenv
import os

# Cargar variables del archivo .env
load_dotenv()

class SingletonMeta(type):
    _instances = {}
    _lock = threading.Lock()  # Asegura que solo haya una instancia en entornos multi-hilo

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]

class PostgresSingleton(metaclass=SingletonMeta):
    def __init__(self):
        self.connection = None
        # Cargar variables desde el archivo .env
        self.db_name = os.getenv('DB_NAME')
        self.db_user = os.getenv('DB_USER')
        self.db_password = os.getenv('DB_PASSWORD')
        self.db_host = os.getenv('DB_HOST')
        self.db_port = os.getenv('DB_PORT')
        self.connect()

    def connect(self):
        if self.connection is None:
            try:
                self.connection = psycopg2.connect(
                    dbname=self.db_name,
                    user=self.db_user,
                    password=self.db_password,
                    host=self.db_host,
                    port=self.db_port
                )
                # Cambia la codificación de cliente a LATIN1 si tus datos están en Latin-1
                self.connection.set_client_encoding('LATIN1')  # O UTF8 si sabes que los datos son UTF-8
                print("Conexión exitosa a la base de datos")
            except OperationalError as e:
                print(f"Error al conectar a la base de datos: {e}")
    
    def get_cursor(self):
        if self.connection:
            return self.connection.cursor()

    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("Conexión cerrada")

    def insert_clima(self, tipo_clima, fecha, hora):
        cursor = self.get_cursor()
        if cursor:
            try:
                cursor.execute(
                    """
                    INSERT INTO registro_clima (tipo_clima, fecha, hora)
                    VALUES (%s, %s, %s);
                    """, 
                    (tipo_clima, fecha, hora)
                )
                self.connection.commit()
                print("Registro insertado con éxito")
            except Exception as e:
                print(f"Error al insertar registro: {e}")
                self.connection.rollback()

# Uso del singleton para conectar a PostgreSQL y realizar una inserción
if __name__ == "__main__":
    # Inicializar la conexión usando las variables del archivo .env
    db = PostgresSingleton()
    
    # Inserción de datos (asegúrate de que ya tienes la tabla 'registro_clima' creada)
    tipo_clima = "Soleado".encode('latin1').decode('latin1')  # Asegúrate de que los datos sean decodificados correctamente
    fecha = datetime.now().date()
    hora = datetime.now().time()

    db.insert_clima(tipo_clima, fecha, hora)

    # Cerrar la conexión
    db.close_connection()
