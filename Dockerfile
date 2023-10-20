FROM python:3.10

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt

COPY app.py /app/
COPY func.py /app/

RUN apt-get update && apt-get install libgl1 -y

EXPOSE 8080/tcp

CMD ["python3","-m","flask","run","--host=0.0.0.0","--port=8080"]