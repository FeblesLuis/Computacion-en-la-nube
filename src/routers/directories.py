from typing import List, Optional
from fastapi import APIRouter, HTTPException
from services.MongoAtlas import MongoDBConnector
from models import DirectoryItem
from fastapi import Body
import json

# Crea un nuevo enrutador (router) para la ruta "/directories"
# y le asigna la etiqueta "directories"
router = APIRouter(
    prefix="/directories",
    tags=["directories"],
)
# Definición del endpoint GET /directories/
# Busca a todos los usuarios
@router.get("/")
def list_directories():
    connector = MongoDBConnector()
    usuarios = connector.read_Users()
    return usuarios


# Definición del endpoint POST /directories/
# Crea un nuevo directorio y lo agrega a la lista de directorios
@router.post("/")
def create_directory(directory: DirectoryItem):

    connector = MongoDBConnector()
    if (connector.read_Id(directory.id)):
        raise HTTPException(status_code=409, detail="User already exist")

    connector.insert_Users(directory)
    return directory


# Definición del endpoint GET /directories/{id}
# Obtiene un directorio específico por su ID
# Si no se encuentra, lanza una excepción HTTP 404
@router.get("/{id}")
def get_directory(id: int):
    connector = MongoDBConnector()
    usuario = connector.read_Id(id)
    return usuario
    raise HTTPException(status_code=404, detail="Directory not found")


# Definición del endpoint PUT /directories/{id}
# Actualiza un directorio existente por su ID
# Si no se encuentra, lanza una excepción HTTP 404
@router.put("/{id}")
def update_directory(id: int, directory: DirectoryItem):
    
    connector = MongoDBConnector()
    # Eliminar el objeto problemático
    connector.delete_Id(id)
    # Volver a subir el objeto corregido
    connector.insert_Users(directory)  


# Definición del endpoint PATCH /directories/{id}
# Actualiza parcialmente un directorio existente por su ID
# Si no se encuentra, lanza una excepción HTTP 404
@router.patch("/{id}")
def update_directory_partial(id: int, directory_update: Optional[DirectoryItem] = None):
    connector = MongoDBConnector()
    user = connector.read_Id(id)
    if (user):
        print("Serealizaron cambios")
        usuario = DirectoryItem(**user)
        if directory_update.path != user.get("path"):
            usuario.path= directory_update.path
            connector.delete_Id(id)
            connector.insert_Users(usuario)
        if directory_update.name != user.get("name"):
            usuario.name= directory_update.name
            connector.delete_Id(id)
            connector.insert_Users(usuario)     
    else:
        print("No se realizaron actualizaciones.")
        raise HTTPException(status_code=409, detail="User already exist")

# Definición del endpoint DELETE /directories/{id}
# Elimina un directorio existente por su ID
# Si no se encuentra, lanza una excepción HTTP 404
@router.delete("/{id}")
def delete_directory(id: int):
    connector = MongoDBConnector()
    usuario = connector.delete_Id(id)
    print(usuario)
    return usuario
    raise HTTPException(status_code=404, detail="Directory not found")