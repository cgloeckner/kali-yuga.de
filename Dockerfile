FROM python:3.10.8-slim

WORKDIR /app

COPY ./requirements.txt /app
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /app

CMD [ "python", "main.py", "-p", "80", "--reverse-proxy" ]
