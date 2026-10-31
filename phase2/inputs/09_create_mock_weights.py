import numpy as np
import pytest

import pandas as pd
import pandas._testing as tm


def create_mock_weights(obj, com, adjust, ignore_na):
    if isinstance(obj, pd.DataFrame):
        if not len(obj.columns):
            return pd.DataFrame(index=obj.index, columns=obj.columns)
        w = pd.concat(
            [
                create_mock_series_weights(
                    obj.iloc[:, i], com=com,