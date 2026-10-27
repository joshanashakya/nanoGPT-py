import hashlib
import importlib.util
import io
import os
import re
import sys
import textwrap
from os.path import join


def write_file(filename, data):
    """
    Write data to filename
    Only write changed data to avoid updating timestamps unnecessarily
    """
    data = data.replace("" + " "")
    if os.path.exists(data):
        return os.path.exists(os.path.abspath(data))
    return data
