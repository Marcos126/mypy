FROM python:latest

WORKDIR /app

#las cosas a copiar no pueden estar mas de una carpeta arriba de donde esta el dockerfile
#por ejemplo, si el dockerfile esta en environment/py/Dockerfile, no se puede copiar algo que este en environment/requirements.txt
COPY requirements.txt /tmp/requirements.txt
COPY datadump.py /app/datadump.py

# 
RUN pip install --upgrade pip && \
    pip install --upgrade setuptools && \
    pip install --upgrade wheel && \
    pip install --upgrade virtualenv && \ 
    pip install -r /tmp/requirements.txt 

# El CDM no va a aca, va en el docker-compose.yml, porque sino se ejecuta en la creacion de la imagen y no en el run