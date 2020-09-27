import numpy as np
import pandas as pd

from .base import NumpyColumn


class NumpyDateTimeColumn(NumpyColumn):
    dtype = np.dtype(np.uint32)
    py_types = (int,)
    format = 'I'

    def __init__(self, timezone=None, **kwargs):
        super(NumpyColumn, self).__init__(**kwargs)
        self.timezone = timezone

    def read_items(self, n_items, buf):
        data = super(NumpyColumn, self).read_items(n_items, buf)
        dt = data.astype('datetime64[s]')
        if self.timezone:
            ts = pd.to_datetime(dt, utc=True)
            dt = ts.tz_convert(self.timezone).tz_localize(None).values
        return dt


def create_numpy_datetime_column(spec, column_options):
    context = column_options['context']

    tz_name = None

    # Use column's timezone if it's specified.
    if spec[-1] == ')':
        tz_name = spec[10:-2]
    else:
        if not context.settings.get('use_client_time_zone', False):
            tz_name = context.server_info.timezone

    return NumpyDateTimeColumn(tz_name)
