FROM ubuntu:latest



RUN apt-get update

RUN apt-get -y install python3


COPY class3-homework.py .

COPY wdbc.data .

CMD ["python3","-u","class3-homework.py"]
