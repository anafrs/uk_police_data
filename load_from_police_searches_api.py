import io
import pandas as pd
import requests
import json
from pandas import json_normalize

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Loading data from API
    """
    
    month_range = pd.period_range(start='2022-06-01', end ='2024-02-01' , freq ='M')
    df_list = []

    for month in month_range:
        url = f'https://data.police.uk/api/stops-street?lat=51.507351&lng=-0.127758&date={month}'
        r = requests.get(url)
        data = r.json()
        df_list.append(pd.json_normalize(data))


        df = pd.concat(df_list)

    return df


@test
def test_output(output, *args) -> None:
    """
    Code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
    assert output.datetime is not None, 'Error: some timestamps are null'
