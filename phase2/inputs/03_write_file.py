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
