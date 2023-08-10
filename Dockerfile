FROM python:3.8-slim-buster
WORKDIR /python-docker
ENV PYTHONUNBUFFERED=1
RUN apt-get update && apt-get install gcc -y && apt-get install libpq-dev -y
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt



COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]