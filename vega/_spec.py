"""
Provides VegaSpec.

"""
from collections import Mapping
import pandas as pd

from ._data import VegaData


class VegaSpec(dict):
    """
    Mapping representing Vega/Vega-Lite spec.
    """

    def __init__(self, spec, data=None, size=None):

        elements = spec.copy()

        if isinstance(size, Mapping):
            for key in ['width', 'height']:
                if key in size:
                    elements[key] = size[key]

        if isinstance(data, pd.DataFrame):
            # We have to do the isinstance test first because we can't
            # compare a DataFrame to None.
            elements['data'] = {'values': VegaData.from_dframe(data)}
        elif isinstance(data, dict):
            elements['data'] = []
            # We have to do the isinstance test first because we can't
            # compare a DataFrame to None.
            for key, value in data.items():
                elements['data'].append(
                    {'name': key, 'values': VegaData.from_dframe(value)}
                )
        elif data is None:
            # Data is either passed in spec or error
            pass
        else:
            # As a last resort try to pass the data to a DataFrame
            # and use it
            df = pd.DataFrame(data)
            elements['data'] = {'values': VegaData.from_dframe(df)}

        super().__init__(**elements)
