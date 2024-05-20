import os
from pymongo import MongoClient
from dotenv import load_dotenv

class MongoConnector:
    def __init__(self):
        load_dotenv(".env")
        try:
            self.client = MongoClient(os.getenv('host'), int(os.getenv('port')))  # Corrección aquí
            db = self.client[str(os.getenv('database_name'))]
            collection = db[os.getenv('collection_name')]
            self.documents = collection.find()
            

        except Exception as ex:
            print("Error al conectar con la BD {}".format(ex))
        finally:
            print("Conexión finalizada")