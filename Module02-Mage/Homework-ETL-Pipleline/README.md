This directory contains the files I used to do the homework tasks.

In this task, I created an ETL pipeline that:
- extracts 3 different datasets from a GitHub repo based on the year and month value supplied ([load_green_taxi_data](load_green_taxi_data.py))
- transforms the data (takes out trips with 0 passengers and 0 distance, creates two columns, renames columns)([transform_green_taxi_data](transform_green_taxi_data.py))
- loads data to a postgresdb ([load_data_to_postgres](load_data_to_postgres.py))
- loads data to a Google Cloud Storage bucket ([load_green_taxi_to_gcs_bucket](load_green_taxi_to_gcs_bucket.py))

Below is an image representation of the pipeline.

![alt text](image.png)

Inside Mage, I declared global variables to hold the year, month and url. I also scheduled the pipeline to run daily at 5AM UTC.