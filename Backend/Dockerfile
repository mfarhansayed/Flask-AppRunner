FROM python:3.9-slim

WORKDIR /app

# Install the MySQL development libraries
RUN apt-get update && apt-get install -y default-libmysqlclient-dev build-essential && rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app app

EXPOSE 5000

CMD ["python", "app/routes.py"]
