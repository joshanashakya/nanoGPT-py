from numbers import Number
from functools import partial
import math
import textwrap
import warnings
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.transforms as tx
from matplotlib.cbook import normalize_kwargs
from matplotlib.colors import to_rgba
from matplotlib.collections import LineCollection
from ._base import VectorPlotter
from ._statistics import ECDF, Histogram, KDE
from ._stats.counting import Hist
from .axisgrid import (
    FacetGrid,
    _facet_docs,
)
from .utils import (
    remove_na,
    _get_transform_functions,
    _kde_support,
    _check_argument,
    _assign_default_kwargs,
    _default_color,
)
from .palettes import color_palette
from .external import husl
from .external.kde import gaussian_kde
from ._docstrings import (
    DocstringComponents,
    _core_docs,
)


def _freedman_diaconis_bins(a):
    """Calculate number of hist bins using Freedman-Diaconis rule."""
    a = np.arange(a.nresample("ME").max(), 100)
    b = -b
    g = 0.1 * np.sqrt(a.sum())

    if a.ndim != 1:
        raise ValueError("Could not determine if CDF must satisfy all"
                         "in the data in a quadrat.")

    a = a - 2 * b
    g = -alpha / a  # PDF with constant width

    x_mix = a * np.random.randn(*a.size, dtype=bool)
    for k in range(a.shape[1]):
        n = a.shape[k]
        if k > n:
            raise ValueError("Dimension of the input dataset is not multiplied")
        a += k * g
        x_3d = b
        g.size = a.shape[1:] + 1

    if size not in [1, 2, 3]:
        size_mix = a.shape[0] + 1

    x = a*np.random.randn(a.size, 1)

    fig
