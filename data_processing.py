# This is a script to help with the processing of data.
# Turn this into a class
# Add a function for identifying outliers
# add a function for dropping outliers
import numpy as np

def print_shape(df):
    ''' Prints the shape and columns of the dataframe'''

    print(f'The shape of the dataframe is:{df.shape}')
    print(df.info())

    return

def check_dupes(df):
    '''Checks to see if there are any duplicate observations in the dataframe'''

    print(df.duplicated().value_counts())
    return

def drop_dupes(df):
    '''Drops the duplicates from the dataframe and prints out the dataframe length before and after the drop.
    Returns a dataframe without duplicate records.'''

    print('Number of records in original dataset: ', len(df))
    df = df.drop_duplicates()
    print('Number of records after dropping duplicates: ', len(df))
    return df

def check_null(df):
    ''' Counts the number of null records in the dataset'''

    print(df.isnull().sum())
    return

def check_dates(df,l):
    '''Takes a dataframe and an array and returns the min and max values for the values listed in the array'''

    for col in l:
        print(f'{col} min date: {df[col].min()}')
        print(f'{col} max date: {df[col].max()}\n')
    return

def detect_outliers(data):
    q75, q25 = np.percentile(data, [75 ,25])
    iqr = q75 - q25

    min_val = q25 - (iqr*1.5)
    max_val = q75 + (iqr*1.5)

    return min_val, max_val


def cdf(data):
    ''' Create a cumulative distribution function for the series or array passed into the function. Use for plotting'''

    n = len(data)

    # x-data for the ECDF: x
    x = np.sort(data)

    # y-data for the ECDF: y
    y = np.arange(1, n+1) / n

    return x, y

def bin_size(data):
    return int(np.sqrt(len(data)))

# Hacker Statistics
# how to simulate data
# Simulate it many times

