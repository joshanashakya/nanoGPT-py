"""Functions to estimate uncertainties such as entropy, KL divergence etc."""

import numpy as np
from numpy.linalg import det
from scipy.special import digamma
from scipy.stats import entropy
from sklearn.neighbors import NearestNeighbors

from dowhy.gcm.constant import EPS
from dowhy.gcm.util.general import shape_into_2d

def estimate_gaussian_entropy(X: np.ndarray) -> float:
    """Entropy with respect to standardized variables."""
    X = shape_into_2d(X)

    if X.shape[1] > 1:
        return 0.5 * np.log((2 * np.pi * np.e) ** X.shape[1] * estimate_variance(X))
    else:
        return 0.5 * np.log(2 * np.pi * np.e * estimate_variance(X))