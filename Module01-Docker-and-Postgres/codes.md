##### command to run a postgres container and specify environment variables

```
docker run -it \
    -e POSTGRES_USER="outis" \
    -e POSTGRES_PASSWORD="****" \
    -e POSTGRES_DB="ny_taxi" \
    -v $(pwd)/ny_taxi_postgres_data:/var/lib/postgresql/data \
    -p 5432:5432 \
    postgres:13
```

##### Download and unzip yellow trips dataset for january 2021
```
wget https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz

gunzip yellow_tripdata_2021-01.csv.gz
```