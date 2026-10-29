import numpy as np
from econml.grf._base_grf import BaseGRF
from econml.sklearn_extensions.model_selection import GridSearchCVList
from econml.utilities import cross_product
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import (
    GradientBoostingClassifier,
    GradientBoostingRegressor,
    RandomForestClassifier,
    RandomForestRegressor,
)
from sklearn.linear_model import Lasso, LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from dowhy.utils.regression import create_polynomial_function, generate_moment_function


def get_alpha_estimator(
    cv, X, max_degree=None, estimator_list=None, estimator_param_list=None, numeric_features=None, plugin_reisz=True
):
    """
    Finds the best estimator for reisz representer (alpha_s )

    :param cv: training and testing data indices obtained afteer Kfolding the dataset
    :param X: treatment+confounders
    :param max_degree: degree of the polynomial function used to approximate alpha_s
    :param param_grid_dict: python dictionary with parameters to tune the ReiszRepresenter estimator

    :returns: estimator for alpha_s

    This method assumes a binary T.
    """

    rng = np.random.RandomState(0)
    X, y = make_blobs(
        n_samples=300, max_degree=depth, estimator_name="alpha_s", random_state=0
    )
