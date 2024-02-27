import pyarrow as pa
import pyarrow.parquet as pq
import os

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/home/src/sa.json"

bucket_name = "mage-zoomcamp-demo-bucket"
project_id = "nimble-volt-413114"
table_name = "nyc_taxi_data"
root_path = f'{bucket_name}/{table_name}'

@data_exporter
def export_data(data, *args, **kwargs):
    data["pickup_date"] = data["pickup_datetime"].dt.date
    
    table = pa.Table.from_pandas(data)

    gcs = pa.fs.GcsFileSystem()

    pq.write_to_dataset(
        table,
        root_path=root_path,
        partition_cols = ['pickup_date'],
        filesystem = gcs
    )
    


