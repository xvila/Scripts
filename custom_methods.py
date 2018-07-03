import numpy as np
import pandas as pd

class CustomSeries(pd.Series):
    @property
    def _constructor(self):
        return CustomSeries

    def custom_series_function(self):
        return 'OK'

class DataSet(pd.DataFrame):
    def __init__(self, df, *args, **kw):
        super(DataSet, self).__init__(*args, **kw)
        self.data = df

    @property
    def _constructor(self):
        return DataSet

    _constructor_sliced = CustomSeries

    def print_shape(self):
        ''' Prints the shape and columns of the dataframe'''

        print(f'The shape of the dataframe is:{self.data.shape}')
        print(self.data.info())

        return

    def check_dupes(self):
        '''Checks to see if there are any duplicate observations in the dataframe'''

        return print(self.data.duplicated().value_counts())

    def drop_dupes(self):
        '''Drops the duplicates from the dataframe and prints out the dataframe length before and after the drop.
        Returns a dataframe without duplicate records.'''

        print('Number of records in original dataset: ', len(self.data))
        data = self.data.drop_duplicates()
        print('Number of records after dropping duplicates: ', len(self.data))
        return data

    def check_null(self):
        ''' Counts the number of null records in the dataset'''
        return self.data.isnull().sum()

    def check_dates(self, l):
        '''Takes a dataframe and an array and returns the min and max values for the values listed in the array'''

        for col in l:
            print(f'{col} min date: {self.data[col].min()}')
            print(f'{col} max date: {self.data[col].max()}\n')
        return

    def detect_outliers(self, column):
        q75, q25 = np.percentile(self.data[column], [75, 25])
        iqr = q75 - q25

        min_val = q25 - (iqr*1.5)
        max_val = q75 + (iqr*1.5)

        return min_val, max_val

    def cdf(self):
        ''' Create a cumulative distribution function for the series or array passed into the function. Use for plotting'''

        n = len(self.data)

        # x-data for the ECDF: x
        x = np.sort(self.data)

        # y-data for the ECDF: y
        y = np.arange(1, n+1) / n

        return x, y

    def bin_size(self):
        return int(np.sqrt(len(self.data)))
