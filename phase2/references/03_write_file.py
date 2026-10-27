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
    if os.path.exists(filename):
        with open(filename) as f:
            if data == f.read():
                return

    with open(filename, 'w') as fid:
        fid.write(data)
