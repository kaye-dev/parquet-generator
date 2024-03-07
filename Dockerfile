FROM python:3.9

WORKDIR /app

RUN pip install pandas pyarrow

COPY . /app

CMD ["python", "script.py"]
