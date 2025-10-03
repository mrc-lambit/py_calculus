FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt .
COPY calculus.py ./app.py

RUN pip install -r requirements.txt

CMD ["python", "app.py"]