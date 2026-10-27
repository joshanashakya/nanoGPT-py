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
