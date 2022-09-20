FROM ghcr.io/binkhq/python:3.9-pipenv

WORKDIR /app
ADD . .

RUN pip install --no-cache pipenv

CMD [ "python", "schedule.py" ]
