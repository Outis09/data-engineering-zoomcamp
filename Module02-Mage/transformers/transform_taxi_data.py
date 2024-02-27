if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    # check rows with zero passengers
    rows_w_zero_passengers = (data['passenger_count'] == 0).sum()

    print(f'rows with zero passengers: {rows_w_zero_passengers}')

    # check rows with zero distance
    zero_distance = (data['trip_distance'] == 0 ).sum()
    print(f'trips with zero distance: {zero_distance}')

    # drop rows with 0 passengers and 0 distance
    data = data[(data['passenger_count'] > 0) & (data['trip_distance'] > 0)]

    # new names for undescriptive columns
    new_names = {
        'tpep_pickup_datetime':'pickup_datetime',
        'tpep_dropoff_datetime':'dropoff_datetime',
    }

    data.rename(columns = new_names,inplace=True)
    return data


@test
def test_passengers(output, *args):
    assert (output['passenger_count'] == 0).sum() == 0, 'There are rides with zero passengers'

@test
def test_distance(output, *args):
    assert (output['trip_distance'] == 0).sum() == 0, 'There are rides with zero distance'
