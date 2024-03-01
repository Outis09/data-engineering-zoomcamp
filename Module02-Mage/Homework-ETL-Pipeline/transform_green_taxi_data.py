if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def extract_non_zero(data, *args, **kwargs):
    # check if any trips exist with zero passengers or distance
    rows_with_zero_passengers_and_distance = ((data['passenger_count'] == 0) | (data['trip_distance'] == 0)).sum()
    # drop trips with zero passengers or distance
    if rows_with_zero_passengers_and_distance > 0:
        data = data[(data['passenger_count'] > 0) & (data["trip_distance"] > 0)]
    # create two date columns
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date
    data['lpep_dropoff_date'] = data['lpep_dropoff_datetime'].dt.date
    # make all column names snake case
    data.columns = (data.columns
                .str.replace('(?<=[a-z])(?=[A-Z])', '_', regex=True)
                .str.lower()
             )
    return data

@test
def check_case(output,*args):
    assert 'vendor_id' in output.columns, 'There is a column with CamelCase'


@test
def test_passengers(output, *args) -> None:
    zero_passenger_count = (output['passenger_count'] == 0).sum()
    assert zero_passenger_count == 0, 'There are still trips with 0 passengers'

@test
def test_distance(output, *args) -> None:
    zero_trip_count = (output['trip_distance'] == 0).sum()
    assert zero_trip_count == 0, 'There are still trips with 0 trip distance'