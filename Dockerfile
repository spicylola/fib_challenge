FROM python:3.7.0-alpine

RUN apk add --no-cache python3-dev libffi-dev gcc musl-dev make

WORKDIR /fib_challenge

COPY . /fib_challenge

RUN pip install -r requirements.txt

CMD [ "python", "start_app.py" ]