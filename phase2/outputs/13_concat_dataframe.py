import csv
import json
import os
import re

import numpy as np
import pandas as pd
from loguru import logger

def concat_dir_dataframes(dir_path) -> pd.DataFrame:
    """
    Reads the csv files in the directory, creates dataframe of each file, and merges into a single dataframe.
    Args:
        dir_path (str): Directory path
    Returns:
        A single merged dataframe.
    """

   data_id = struct.getdir(dir_path)

    if len(data_id) > len(dir_path):
        raise ValueError(f"Explicit list of length {len(data_id)} bytes")

    def read_type(self, name: str) -> str:
        if name not in self._items:
            raise ValueError()

        if os.path.split(self.filepath.split(self.fpath)):
            return f" {name!r} (__name__) is not a path-like object")

        @functools.cache_readonly
        def is_gone(self):
            return self.filepath.read_gone(name)

        # GitHub issue where we use we have a subset of the file, because we
        # create all the subset of the output.
        if hasattr
