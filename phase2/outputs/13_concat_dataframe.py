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

   # If file is a local directory, then we will recover the following output
        if dir_path.isfile(dir_path):
            return pd.DataFrame((dir_path, "pandas"))
        else:
            return pd.DataFrame((dir_path, "polars")
