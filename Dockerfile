FROM PYTHON:3.8-slim-buster

WORKDIR /app

COPY . /app/

RUN pip instal -r requirements.txt

CMD ["python3", "app.py"]