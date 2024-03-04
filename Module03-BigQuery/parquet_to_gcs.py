from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.google_cloud_storage import GoogleCloudStorage
from pandas import DataFrame
#from os import path
import os

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_google_cloud_storage(output, **kwargs) -> None:
    # loop through files in directory
    for filename in os.listdir(output):
        # if file is a parquet file
        if filename.endswith('.parquet'):
            
            config_path = os.path.join(get_repo_path(), 'io_config.yaml')
            config_profile = 'default'

            # fullpath to file
            fullpath = f'{output}{filename}'
            bucket_name = 'green_trip_data'
            object_key = f'{filename}'

            # save file to GCS bucket
            GoogleCloudStorage.with_config(ConfigFileLoader(config_path, config_profile)).export(
                fullpath,
                bucket_name,
                object_key,
            )
