

# Establece la imagen base para construir la imagen de Docker
FROM python:3.9

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos de requerimientos y los instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de los archivos del proyecto al contenedor
COPY . .

# Expone el puerto en el que se ejecutará tu aplicación
EXPOSE 8000

# Comando para iniciar tu aplicación
CMD ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000"]