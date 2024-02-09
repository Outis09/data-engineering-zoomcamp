##### command to run a postgres container and specify environment variables

```
docker run -it \
    -e POSTGRES_USER="outis" \
    -e POSTGRES_PASSWORD="****" \
    -e POSTGRES_DB="ny_taxi" \
    -v $(pwd)/ny_taxi_postgres_data:/var/lib/postgresql/data \
    -p 5432:5432 \
    postgres:13