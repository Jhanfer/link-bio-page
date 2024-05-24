# Este Dockerfile es usado para desplegar un contenedor simple de una instancia de Reflex 

# Se establece la versión de Python a utilizar
FROM python:3.11


# Creando un directorio de trabajo llamado "/app"
WORKDIR /app
# Compiar el contenido a "/app" dentro del contenedor 
COPY . .

# Creamos la variable donde se va a guardar el entorno virtual - Es recomendable cambiar el nombre del ".venv" a ".venv_[CUALQUIERCOSA]" para evitar confusiones o incompatibilidad
ENV VIRTUAL_ENV=/app/.venv_docker

# Añadir al "PATH" el entorno virtual que hemos creado antesz
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Ejecutar el comando de Python para crear el entorno virtual
RUN python3.11 -m venv $VIRTUAL_ENV

# Acrualizar pip
RUN pip install --upgrade pip

# Instalar los requerimientos sin caché
RUN pip install --no-cache-dir -r requirements.txt


# Lanzar el Backend - "--env prod" es para lanzarlo a producción - "--backend-only" es para lanzar solo el backend
CMD [ -d alembic ] && reflex db migrate; reflex run --env prod --backend-only