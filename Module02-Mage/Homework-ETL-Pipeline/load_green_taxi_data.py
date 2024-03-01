import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    # retrieve defined global variables
    year = kwargs['year']
    months = kwargs['months']
    base_url = kwargs['base_url']
    # create empty list
    dataframes = []
    # specify dtype of columns
    dtypes = {
        'VendorID' : pd.Int64Dtype(),
        'store_and_fwd_flag' : str,
        'RatecodeID' : pd.Int64Dtype(),
        'PULocationID'  :pd.Int64Dtype(),
        'DOLocationID':pd.Int64Dtype(),
        'passenger_count' : pd.Int64Dtype(),
        'payment_type' : pd.Int64Dtype(),
        'fare_amount':float,
        'trip_distance':float,
        'extra':float,
        'mta_tax':float,
        'tip_amount':float,
        'tolls_amount':float,
        'ehail_fee':float,
        'improvement_surcharge':float,
        'total_amount':float,
        'trip_type':str,
        'congestion_surcharge':float

    }

    # specify date columns
    parse_dates = ['lpep_pickup_datetime','lpep_dropoff_datetime']
    # loop through months
    for month in months:
        # file for each month
        filename = f'green_tripdata_{year}-{month}.csv.gz'
        url = f'{base_url}/{filename}'
        # read data for month
        data = pd.read_csv(url, sep=',',compression='gzip',dtype=dtypes,parse_dates=parse_dates)
        # append data to list
        dataframes.append(data)
    # response = requests.get(url)

    # return dataframe extracted from list
    return pd.concat(dataframes,ignore_index=True) 


@test
def test_output(output, *args):
    assert output is not None, 'The output is undefined'
