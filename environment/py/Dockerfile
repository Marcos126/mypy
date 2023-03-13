#Imagen que se va a usar en el contenedor
FROM mysql:latest

#Variables de entorno para la configuración de la base de datos
ENV MYSQL_DATABASE=lomas \
    MYSQL_USER=marco \
    MYSQL_PASSWORD=lomas \
    MYSQL_ROOT_PASSWORD=useyourilussioN

#Variable para exponer el puerto 3306
EXPOSE 3306

#Comando que se va a ejecutar al iniciar el contenedor

CMD ["mysqld"]

#imagen que se va a usar en el contenedor 
FROM python:latest

#Carpeta que se va a crear en el contenedor
WORKDIR /app

COPY ./datadump.py /app/datadump.py 
COPY ./requirements.txt /tmp/requirements.txt

RUN pip install --upgrade pip &&\
    pip install -r /tmp/requirements.txt

CMD [ "sleep 10 && datadump.py" ] 

    