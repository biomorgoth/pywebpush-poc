FROM python:3.10-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app app

ENV FLASK_APP=app

CMD [ "flask", "run", "--host=0.0.0.0" ]