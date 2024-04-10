import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(df, *args, **kwargs):
    """
    Casts the datetime column to datetime
    Creates a separate column for date
    Replaces the dot in the column name with an underscore
    """
    # Specify your transformation logic here

    #changes date to datetime
    df['datetime'] = pd.to_datetime(df['datetime'])

    # creates column for the date only

    df['date'] = df['datetime'].dt.date

    # replaces . for _ in the column name
    df.columns = df.columns.str.replace('.','_')
    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
