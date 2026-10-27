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