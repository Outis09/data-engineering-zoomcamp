##### command to run a postgres container and specify environment variables

```bash
docker run -it \
    -e POSTGRES_USER="outis" \
    -e POSTGRES_PASSWORD=${POSTGRES_PWD} \
    -e POSTGRES_DB="ny_taxi" \
    -v $(pwd)/ny_taxi_postgres_data:/var/lib/postgresql/data \
    -p 5432:5432 \
    postgres:13
```

##### Download and unzip yellow trips dataset for january 2021
```bash
wget https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz

gunzip yellow_tripdata_2021-01.csv.gz
```

##### Connect to a postgres database using pgcli
```
pgcli -h localhost -u outis -d ny_taxi
```


##### create a network in docker
```bash
docker network create db-network
```

##### run a postgres container in a docker network
```bash
docker run -it \
    -e POSTGRES_USER="outis" \
    -e POSTGRES_PASSWORD=${POSTGRES_PWD} \
    -e POSTGRES_DB="ny_taxi" \
    -v /home/ayersamuel/Documents/data-engineering-zoomcamp/ny_taxi_postgres_data:/var/lib/postgresql/data \
    -p 5432:5432 \
    --network=db-network \
    --name postgres-db \
    postgres:13
```

##### Run a pgadmin container in a network and specify environment variables
```bash
docker run -it \
    -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
    -e PGADMIN_DEFAULT_PASSWORD=${PGADMIN_PASSWORD} \
    -p 8080:80 \
    --network=db-network \
    --name pgadmin \
    dpage/pgadmin4
```

##### Convert notebook to python script
```bash
jupyter nbconvert Upload-data.ipynb --to script
```

##### Rename file to Ingest-data.py
```bash
mv Upload-data.py Ingest-data.py
```

##### Run ingest data script with python
```bash
python Ingest-data.py \
    --user=outis \
    --host=localhost \
    --port=5432 \
    --db=ny_taxi \
    --table_name=yellow_taxi_2021_01_data \
    --url=https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz
```

##### dockerize ingest data script
```bash
docker build -t taxi_ingest:0.2 .
```

##### run docker container with ingest data script
```bash
docker run \
    --network=db-network taxi_ingest:0.2 
    --user=outis 
    --password=${POSTGRES_PWD} 
    --host=postgres-db 
    --port=5432 
    --db=ny_taxi 
    --table_name=yellow_taxi_2021_01_data 
    --url=https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz 
```