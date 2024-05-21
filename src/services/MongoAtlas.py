import os
from typing import List
from dotenv import load_dotenv
from pymongo import MongoClient

class MongoDBConnector:
    def __init__(self):
        load_dotenv(".env")
        try:
            self.client = MongoClient(os.getenv('host'), int(os.getenv('port')))
            db_name = os.getenv('database_name')
            self.db = self.client[db_name]

            # Verificar si la base de datos ya existe
            db_list = self.client.list_database_names()
            if db_name not in db_list:
                # Si no existe, crearla
                self.db.command("create", db_name)
                print("La base de datos '{}' ha sido creada exitosamente.".format(db_name))

            collection_name = os.getenv('collection_name')
            self.collection = self.db[collection_name]
            self.documents = self.collection.find()
            print("Conexión establecida con éxito")
        except Exception as ex:
            print("Error al conectar con la BD:", ex)
        finally:
            print("Conexión finalizada")

    #Funcion que insertadatos en la tabla usuarios
    #
    def insert_Users(self, document): 
        self.client = MongoClient(os.getenv('host'), int(os.getenv('port')))
        db = self.client[str(os.getenv('database_name'))]
        collection = db[os.getenv('collection_name')]
        self.documents = collection.find()
        
        result = collection.insert_one(document.__dict__)
        return result.inserted_id
    
    #Funcion que busca todos los usuarios en la tabla users
    #
    def read_Users(self): 
        # Conectarse a la base de datos en MongoDB Atlas
        self.client = MongoClient(os.getenv('host'), int(os.getenv('port')))
        db = self.client[str(os.getenv('database_name'))]
        collection = db[os.getenv('collection_name')]
        self.documents = collection.find()
        # Realizar la búsqueda del usuario por nombre
        usuarios = collection.find()
        lista = []
        for usuario in usuarios:
            dic = {}
            dic["id"] = str(usuario['id'])
            dic["path"] = usuario['path']
            dic["name"] = usuario['name']
            dic["emails"] = usuario['emails']
            lista.append(dic)
        # Imprimir los resultados
        return lista
    
    
    #Funcion que Busca en la tabla un ID
    #
    def read_Id(self, id):
        # Conectarse a la base de datos en MongoDB Atlas
        self.client = MongoClient(os.getenv('host'), int(os.getenv('port')))
        db = self.client[str(os.getenv('database_name'))]
        collection = db[os.getenv('collection_name')]
        self.documents = collection.find()
        # Realizar la búsqueda del usuario por id
        usuarios = collection.find()
        dic = {}
        for usuario in usuarios:
            if usuario['id'] == id:
                dic["id"] = str(usuario['id'])
                dic["path"] = usuario['path']
                dic["name"] = usuario['name']
                dic["emails"] = usuario['emails']
        # Imprimir los resultados
        return dic
    # Función para actualizar un registro por ID en la tabla Users   
    #
    def delete_Id(self, id):
        # Conectarse a la base de datos en MongoDB Atlas
        self.client = MongoClient(os.getenv('host'), int(os.getenv('port')))
        db = self.client[str(os.getenv('database_name'))]
        collection = db[os.getenv('collection_name')]
        self.documents = collection.find()
        # Eliminar el registro que coincide con el ID
        result = collection.delete_one({"id": id})
        # Verificar si se eliminó correctamente
        if result.deleted_count == 1:
            return "Registro eliminado exitosamente."
        else:
            return "No se encontró ningún registro coincidente."