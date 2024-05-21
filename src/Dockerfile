# Establece la imagen base para construir la imagen de Docker
FROM python:3.9

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos de requerimientos y los instala
COPY . /app

# Instala las dependencias del proyecto
RUN pip install -r requirements.txt

# Expone el puerto en el que se ejecutará tu aplicación
# EXPOSE 8000

# Comando para iniciar tu aplicación usando uvicorn
# CMD ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000"]
