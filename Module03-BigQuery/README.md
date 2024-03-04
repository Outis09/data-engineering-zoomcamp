In this module, I learnt data warehousing using BigQuery.

There is not much to show here aside the homework.

The homework can be found [here](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/cohorts/2024/03-data-warehouse/homework.md).

For the homework, I had to download a list of parquet files from a website. The parquet files were the trip data for 2022. I wanted to do this in such a way that it can be repeated and automated easily so I opted to use a data orchestrator, Mage.

In Mage, I used a [data loader](extract_parquet_files.py) to download the data from the website and used a [data exporter](parquet_to_gcs.py) to export the parquet files to a GCS bucket. From there, I used queries in BigQuery to create tables out of the parquet files.

Below are the queries I ran in BigQuery.

##### Create an external table using the Green Taxi Trip Records Data for 2022.

```sql
CREATE EXTERNAL TABLE `project-id.ny_taxi.external_green_tripdata_2022`
  OPTIONS (
    format ="PARQUET",
    uris = ['gs://green_trip_data/*.parquet']
    );
```

##### Create a table in BQ using the Green Taxi Trip Records for 2022 (do not partition or cluster this table).

```sql
CREATE OR REPLACE TABLE project-id.ny_taxi.green_tripdata_2022 
AS 
    SELECT * 
    FROM project-id.ny_taxi.external_green_tripdata_2022;
```

##### Question 1: What is count of records for the 2022 Green Taxi Data?

```sql
SELECT COUNT(lpep_pickup_datetime) 
FROM ny_taxi.green_tripdata_2022;
```
The count of records is 840402

##### Question 2: Write a query to count the distinct number of PULocationIDs for the entire dataset on both the tables.
##### What is the estimated amount of data that will be read when this query is executed on the External Table and the Table?

```sql
SELECT COUNT(DISTINCT PULocationID) 
FROM ny_taxi.green_tripdata_2022;
```

```sql
SELECT COUNT(DISTINCT PULocationID) 
FROM ny_taxi.external_green_tripdata_2022;
```

The estimated amount of data that will be read from the when the query is executed is 6.41MB for the materialized table and 0MB for the external table.

##### Question 3: How many records have a fare_amount of 0?

```sql
SELECT COUNT(lpep_pickup_datetime) 
FROM `ny_taxi.green_tripdata_2022` 
WHERE fare_amount = 0;
```

1622 records have a fare amount of 0

##### Question 4: What is the best strategy to make an optimized table in Big Query if your query will always order the results by PUlocationID and filter based on lpep_pickup_datetime? (Create a new table with this strategy)

The best strategy is to partition by lpep_pickup_datetime and cluster by PULocationID.

```sql
CREATE OR REPLACE TABLE project-id.ny_taxi.partitioned_clustered_green_tripdata_2022
PARTITION BY DATE(lpep_pickup_datetime)
CLUSTER BY PULocationID
AS
  SELECT * FROM `ny_taxi.external_green_tripdata_2022`;
```

##### Question 5: Write a query to retrieve the distinct PULocationID between lpep_pickup_datetime 06/01/2022 and 06/30/2022 (inclusive)
##### Use the materialized table you created earlier in your from clause and note the estimated bytes. Now change the table in the from clause to the partitioned table you created for question 4 and note the estimated bytes processed. What are these values?

From the partitioned and clustered table
```sql
SELECT DISTINCT PULocationID
FROM `ny_taxi.partitioned_clustered_green_tripdata_2022`
WHERE DATE(lpep_pickup_datetime) BETWEEN '2022-06-01' AND '2022-06-30';
```
The size is 1.12MB.

From the previous materialized table
```sql
SELECT DISTINCT PULocationID
FROM `ny_taxi.green_tripdata_2022`
WHERE DATE(lpep_pickup_datetime) BETWEEN '2022-06-01' AND '2022-06-30';
```
The size is 12.82MB.

##### Question 6: Where is the data stored in the External Table you created? 
Answer: GCP Bucket

##### Question 7: It is best practice in Big Query to always cluster your data
Answer: False

##### Question 8 (optional): Write a SELECT count(*) query FROM the materialized table you created. How many bytes does it estimate will be read? Why?

```sql
SELECT COUNT(*) FROM `ny_taxi.partitioned_clustered_green_tripdata_2022`;
```

The query is estimated to read 0 bytes. Due to the partitions and clusters, BigQuery does not need to scan any data to return the result.