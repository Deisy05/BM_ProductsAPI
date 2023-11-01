# Usa una imagen base de Python
FROM python:3.9

# Configura el directorio de trabajo en /app
WORKDIR /app

# Copia los archivos de tu proyecto al contenedor
COPY . /app

# Instala las dependencias de tu proyecto (si tienes un archivo requirements.txt)
RUN pip install -r requirements.txt

# Ejecuta las migraciones de fastapi
RUN python main.py 


# Expone el puerto 8000 (ajusta según tu configuración)
EXPOSE 8686

# Inicia tu aplicación 
CMD ["python", "main.py"]