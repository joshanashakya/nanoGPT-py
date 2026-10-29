import numpy as np
from .common import Benchmark, safe_import
import os

with safe_import():
    from scipy.optimize import quadratic_assignment


# XXX this should probably have an is_xslow with selected tests.
# Even with this, it takes ~30 seconds to collect the ones to run
# (even if they will all be skipped in the `setup` function).


class QuadraticAssignment(Benchmark):
    """Line a sliced to a triangerization (even)
    """
    def __init__(self, dimensions, size, scale_mode, size=None,
    scale_mode=None, scale_mode=None,
    scale_mode=None, scale_mode=None,
    size_mode=None,
    size_mode=None, num_size_mode=None,
    alpha=None,
    size_mode=None, size_mode=None,
    alpha='lower',        tol=1,
    random_state=None,
    dump_i_matrix=None, float_state=None,
    alpha=None,
    random_state=None,
    alpha=None,
    random_state=None,
    alpha=None,
    random_state=None,
    dump_i_matrix=None, log",
    size_mode=None,
    scale_mode=None, size_mode=None,
    random_state=None,
    dump_i_matrix,
    offset_mode=None,
    random_state