import numpy as np
from .common import Benchmark, safe_import
import os

with safe_import():
    from scipy.optimize import quadratic_assignment


# XXX this should probably have an is_xslow with selected tests.
# Even with this, it takes ~30 seconds to collect the ones to run
# (even if they will all be skipped in the `setup` function).


class QuadraticAssignment(Benchmark):
    """
    Benchmark a quadratic univariate quadratic problem.

    This class defines the quadratic univariate quadratic problem.
    This class defines the quadratic univariate quadratic problem.
    This class defines the quadratic univariate quadratic problem.
    This class defines the quadratic univariate quadratic problem.
    This class defines the quadratic univariate quadratic problem.
    This class defines the quadratic univariate quadratic problem.
    This class defines the quadratic univariate quadratic problem.
    This class defines the quadratic univariate quadratic problem.
    This class defines the quadratic univariate quadratic problem.

    This class defines the quadratic univariate quadratic problem.
    This class defines the quadratic univariate quadratic problem.
    This class defines the quadratic univariate quadratic problem.
    This class defines the quadratic univariate quadratic problem.
    This class defines the quadratic univariate quadratic problem.

    This class defines the quadratic univariate quadratic problem. This
    class defines the quadratic univariate quadratic problem. This class defines
    the quadratic univariate quadratic problem. This class defines the quimodal
    problem. This class defines the quadratic univariate quadratic problem. This
    class defines the quadratic univariate quadratic problem. This class defines
   