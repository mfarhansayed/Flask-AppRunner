FROM  python:3.13.0b4-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY ./src .

EXPOSE 5000

ENTRYPOINT ["python3"]
CMD ["app.py"]