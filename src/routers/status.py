from fastapi import APIRouter


# Crea un nuevo enrutador (router) para la ruta "/status"
# y le asigna la etiqueta "status"
router = APIRouter(
    prefix="/status",
    tags=["status"],
)

# Definición del endpoint GET /status/
# Devuelve un objeto JSON con el estado "pong"
@router.get("/")
def get_status():
    return {"status": "pong"}
