##### Created a docker network for postgres and pgadmin
```bash
docker network create homework-db-network
```

##### run a postgres container
```bash
docker run -it \
    -e POSTGRES_USER="homework" \
    -e POSTGRES_PASSWORD=$POSTGRES_PWD \
    -e POSTGRES_DB="ny_taxi" \
    -v /home/ayersamuel/Documents/Volumes/homework01_volume:/var/lib/postgresql/data \
    -p 5432:5432 \
    --network=homework-db-network \
    --name homework-postgres-db \
    postgres:15
```

##### test connection to postgres db in container
```bash
    pgcli -h localhost -u homework -d ny_taxi
```

##### Run a pgadmin container in the same network
```bash
    docker run -it \
    -e PGADMIN_DEFAULT_EMAIL="homework@homework.com" \
    -e PGADMIN_DEFAULT_PASSWORD=$PGADMIN_PWD \
    -p 8080:80 \
    --network=homework-db-network \
    --name homework_pgadmin \
    dpage/pgadmin4
```

##### download greentaxi dataset
```bash
wget -O - https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-09.csv.gz | gunzip green_taxi_data.csv
```

##### download zones dataset
```bash
    wget https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv
```

##### query to answer question 3
```sql
SELECT COUNT(*)
FROM green_taxi_data 
WHERE DATE(lpep_pickup_datetime) = '2019-09-18' 
	AND DATE(lpep_dropoff_datetime) = '2019-09-18';
```

### query to answer question 4
```sql
SELECT DATE(lpep_pickup_datetime), MAX(trip_distance)
FROM green_taxi_data
GROUP BY DATE(lpep_pickup_datetime)
ORDER BY  MAX(trip_distance) DESC
LIMIT 1;
```

##### query to answer question 5
```sql
SELECT t."Borough",sum(g."total_amount")
FROM green_taxi_data g
JOIN taxi_zones t
ON g."PULocationID" = t."LocationID"
GROUP BY t."Borough"
HAVING sum(g."total_amount") > 50000
ORDER BY 2 DESC
LIMIT 3;
```

##### query to answer question 6
```sql
SELECT du."Zone"
FROM green_taxi_data g
JOIN taxi_zones pu
ON g."PULocationID" = pu."LocationID"
JOIN taxi_zones du
ON g."DOLocationID" = du."LocationID"
WHERE pu."Zone" = 'Astoria' and DATE_TRUNC('month',g."lpep_pickup_datetime") = '2019-09-01'
ORDER BY g."tip_amount" DESC
LIMIT 1;
```