import io
import pandas as pd
import requests
import os
from bs4 import BeautifulSoup
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

# empty list to hold parquet URLs
parquet_urls = []

@data_loader
def load_data_from_api(*args, **kwargs):
    # url for data
    url = 'https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page'
    # get url
    response = requests.get(url)

    # if get was successful, scrape url
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # look for urls to parquet files and append to list
        for link in soup.find_all('a', href=True):
            href = link['href']
            if '.parquet' in href and 'green_tripdata_2022' in href:
                parquet_urls.append(href)

    # if urls to parquet files exist, download and save them to a folder
    if len(parquet_urls) != 0:
        # extract first url from list
        first_url = parquet_urls[0]
        # extract file name from url
        filename = first_url.split('/')[-1]
        # extract name to be used as folder name
        foldername = filename.split('-',1)[0]
        # create a folder path
        folderpath = f'/home/src/{foldername}/'
        # create folder is it does not exist
        if not os.path.exists(folderpath):
            os.makedirs(folderpath)
        # download parquet files and save to folder
        for url in parquet_urls:
            # get filename from url
            filename = url.split('/')[-1]
            # get path to file
            filepath = f'/home/src/green_tripdata_2022/{filename}'

            # get url
            response = requests.get(url)
            # if get was successful
            if response.status_code == 200:
                # write to file
                with open(filepath, "wb") as file:
                    file.write(response.content)
            
    # return the folder path to be used in the data exportation
    return folderpath


@test
def check_urls_exist(*args):
    '''
    Test to check if the code retrieved the urls to the parquet files or not
    '''
    assert parquet_urls, 'No parquet URLs were found'




