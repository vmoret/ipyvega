"""
Provides data parser for Vega.
"""
import numpy as np
import pandas as pd


def _sanitize(data):
    """
    Sanitize a DataFrame to prepare it for serialization.

    * Make a copy
    * Raise ValueError if it has a hierarchical index.
    * Convert categoricals to strings.
    * Convert np.int dtypes to Python int objects
    * Convert floats to objects and replace NaNs by None.
    * Convert DateTime dtypes into appropriate string representations

    Parameters
    ----------
    data : pandas.DataFrame
        A pandas dataframe
    """

    df = data.copy()

    if isinstance(df.index, pd.core.index.MultiIndex):
        raise ValueError('Hierarchical indices not supported')
    if isinstance(df.columns, pd.core.index.MultiIndex):
        raise ValueError('Hierarchical indices not supported')

    for col_name, dtype in df.dtypes.iteritems():
        if str(dtype) == 'category':
            # XXXX: work around bug in to_json for categorical types
            # https://github.com/pydata/pandas/issues/10778
            df[col_name] = df[col_name].astype(str)
        elif np.issubdtype(dtype, np.integer):
            # convert integers to objects; np.int is not JSON serializable
            df[col_name] = df[col_name].astype(object)
        elif np.issubdtype(dtype, np.floating):
            # For floats, convert nan->None: np.float is not JSON serializable
            col = df[col_name].astype(object)
            df[col_name] = col.where(col.notnull(), None)
        elif str(dtype).startswith('datetime'):
            # Convert datetimes to strings
            # astype(str) will choose the appropriate resolution
            df[col_name] = df[col_name].astype(str).replace('NaT', '')

    return df


class VegaData(list):
    """
    Represents a list of data records.
    """

    @classmethod
    def from_dframe(cls, data):
        """
        Initializes class from a pandas DataFrame.

        Parameters
        ----------
        data : pd.DataFrame
            A pandas DataFrame with the data.
        """

        if not isinstance(data, pd.DataFrame):
            raise TypeError('Expected type of `data` to be a pandas DataFrame')

        sanitized_data = _sanitize(data)

        return cls(sanitized_data.to_dict(orient='records'))
