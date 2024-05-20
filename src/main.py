from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import directories
from routers import status

import uvicorn

app = FastAPI()

# Configurar CORS
origins = [
    "http://localhost:3000",  # Reemplaza con la URL de tu frontend React
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar los enrutadores en la aplicación
app.include_router(directories.router)
app.include_router(status.router)


# Punto de entrada principal
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)