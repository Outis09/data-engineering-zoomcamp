##### command to run a postgres container and specify environment variables

```bash
docker run -it \
    -e POSTGRES_USER="outis" \
    -e POSTGRES_PASSWORD="****" \
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
    -e POSTGRES_PASSWORD="outis" \
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
    -e PGADMIN_DEFAULT_PASSWORD="outis" \
    -p 8080:80 \
    --network=db-network \
    --name pgadmin \
    dpage/pgadmin4
```