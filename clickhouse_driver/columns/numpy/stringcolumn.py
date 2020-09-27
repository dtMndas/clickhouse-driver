import numpy as np

from .base import NumpyColumn


class NumpyStringColumn(NumpyColumn):
    dtype = np.dtype('object')

    def read_items(self, n_items, buf):
        return np.array(buf.read_strings(n_items, decode=True))
