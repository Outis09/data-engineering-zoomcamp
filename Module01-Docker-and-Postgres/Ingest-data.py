#!/usr/bin/env python
# coding: utf-8

# import modules
import os
import pandas as pd
from sqlalchemy import create_engine
import argparse
#import getpass


def main(arguments):
    user = arguments.user
    host = arguments.host
    port = arguments.port
    db = arguments.db
    table_name = arguments.table_name
    url = arguments.url
    password = arguments.password
    csv_filename = 'output.csv'

    # download data
    os.system(f"wget -O - {url} | gunzip > {csv_filename}")
    
    # # get password for postgres user securely
    # password = getpass.getpass(prompt='Enter password for postgres user: ')

    # create postgres engine
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    # read data in chunks of 100,000
    df_iterator = pd.read_csv(csv_filename,iterator=True,chunksize=100000)

    # extract first chunk in iterator
    df = next(df_iterator)

    # convert columns into datetime
    df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])
    df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])

    # create table with just column headers
    df.head(n=0).to_sql(name=table_name, con=engine,if_exists="replace")

    # add first 100000 rows of data to table
    df.to_sql(name=table_name,con=engine,if_exists='append')

    # add remaining chunks of data to table
    try:
        while True:
            df = next(df_iterator)
            
            df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])
            df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])

            df.to_sql(name=table_name,con=engine,if_exists='append')

            print('rows inserted successfully...')

    except StopIteration:
        print("Successfully added all rows")

if __name__ == '__main__':

    # create parameters
    parser = argparse.ArgumentParser('Ingest CSV data to Postgres')
    parser.add_argument('--user',help='Enter name of postgres user')
    parser.add_argument('--password',help='Enter password')
    parser.add_argument('--host', help='Enter host of postgres')
    parser.add_argument('--port',help='Enter port')
    parser.add_argument('--db',help='database name for postgres')
    parser.add_argument('--table_name',help='enter name of table where data will be ingested')
    parser.add_argument('--url',help='Enter url of csv file')

    args = parser.parse_args()

    main(args)