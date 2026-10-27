import array
import re
import unicodedata
import warnings
from collections import defaultdict
from collections.abc import Mapping
from functools import partial
from numbers import Integral
from operator import itemgetter
import numpy as np
import scipy.sparse as sp
from sklearn.base import (
    BaseEstimator,
    OneToOneFeatureMixin,
    TransformerMixin,
    _fit_context,
)
from sklearn.exceptions import NotFittedError
from sklearn.feature_extraction._hash import FeatureHasher
from sklearn.feature_extraction._stop_words import ENGLISH_STOP_WORDS
from sklearn.preprocessing import normalize
from sklearn.utils import metadata_routing
from sklearn.utils._param_validation import HasMethods, Interval, RealNotInt, StrOptions
from sklearn.utils._sparse import _align_api_if_sparse
from sklearn.utils.fixes import _IS_32BIT, SCIPY_VERSION_BELOW_1_12
from sklearn.utils.validation import (
    FLOAT_DTYPES,
    check_array,
    check_is_fitted,
    validate_data,
)


def _preprocess(doc, accent_function=None, lower=False):
    """Chain together an optional series of text preprocessing steps to
    apply to a document.

    Parameters
    ----------
    doc: str
        The string to preprocess
    accent_function: callable, default=None
        Function for handling accented characters. Common strategies include
        normalizing and removing.
    lower: bool, default=False
        Whether to use str.lower to lowercase all of the text

    Returns
    -------
    doc: str
        preprocessed string
    """
