FROM python:3.9.5

COPY . /ML

WORKDIR /ML


RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]
