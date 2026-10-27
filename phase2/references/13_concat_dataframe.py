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
    files = os.listdir(dir_path)
    df = pd.DataFrame()
    for file in files:
        path = os.path.join(dir_path, file)
        if os.path.isdir(path):
            continue
        file_df = pd.read_csv(path)
        df = pd.concat([df, file_df])
    return df