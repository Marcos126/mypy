FROM python:latest

WORKDIR /app

COPY requirements.txt /tmp/requirements.txt
COPY datadump.py /app/datadump.py

RUN pip install --upgrade pip && \
    pip install --upgrade setuptools && \
    pip install --upgrade wheel && \
    pip install --upgrade virtualenv && \ 
    pip install -r /tmp/requirements.txt 

CMD [ "python", "datadump.py" ]