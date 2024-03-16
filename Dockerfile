FROM python:3.10

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 3100

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3100"]