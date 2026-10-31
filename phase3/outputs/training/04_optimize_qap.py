import numpy as np
from .common import Benchmark, safe_import
import os

with safe_import():
    from scipy.optimize import quadratic_assignment


# XXX this should probably have an is_xslow with selected tests.
# Even with this, it takes ~30 seconds to collect the ones to run
# (even if they will all be skipped in the `setup` function).


class QuadraticAssignment(Benchmark):
    """ Benchmarks for the quadratic computation in parallel."""

    # XXX this should probably have anis_xslow with selected tests.

    def _get_non_bounds(xslow, x, bounds, bounds, searchsorted,
                 constraints, searchsorted,
                 constraints_function, constraints_function):
        return x[0], x[1] + args[0]

    def _get_non_bounds(xslow, x, bounds, searchsorted, constraint):
        return x[0] + args[1] + args[0] + args[2] + args[0]

    def _get_non_bounds(xslow, x, bounds, searchsorted,
                 constraints_function, constraints, searchsorted, constraints_function):
        return ([4] * x[:-1], *x[-1]) + (x[:-1], *x[-1]) - (x[-2]) +  x[-3]

    def _get_nonbounds(xslow, x, bounds, searchsorted, constraints_function):
        return ((x : (x[0], x[-1]))) / (