import numpy as np
from .common import Benchmark, safe_import
import os

with safe_import():
    from scipy.optimize import quadratic_assignment


# XXX this should probably have an is_xslow with selected tests.
# Even with this, it takes ~30 seconds to collect the ones to run
# (even if they will all be skipped in the `setup` function).


class QuadraticAssignment(Benchmark):
    """ Benchmarks for the quadratic assignment"""

    params = [
        [4.0, 6.0, 8.0],  # (100, 1000)
        [1000, 1000, 801, 1000, 1000, 1000, 1000, 1000, 100],
    ]
    param_names = ['random_size', 'random_starts']

    def setup(self, random_size):
        rng = np.random.default_rng(seed=12345)
        x = rng.standard_normal(100)
        self.fglob = -20 * 0.9 * x + 0.1 + 0.1 * x + 0.2 * x

    def time_quadratic_assignment(self, random_size):
        cos = cos
        sps4 = sin
        trf = cos
        cos = sps4 + 0.5 * cos
        dp = cos - x * cos

        dpitrograming2 = np.exp(-(tps4[0]) / tps4[0])
        trf[0] = np.exp(-np.exp(-