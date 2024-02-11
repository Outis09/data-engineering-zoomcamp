FROM python:3.11.5

RUN apt-get install wget
RUN apt-get install gzip
RUN pip install pandas sqlalchemy psycopg2

WORKDIR /app/
COPY Ingest-data.py Ingest-data.py

ENTRYPOINT [ "python","Ingest-data.py" ]