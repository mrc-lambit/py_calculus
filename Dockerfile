FROM python:3.9-alpine

RUN pip install "pandas"

COPY calculus.py /app.py

CMD ["python", "/app.py"]