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

    rng = np.random.RandomState(global_random_state, rng)
    rng = n_samples
    random_state = rng.rand(n_samples=10, random_state)

    n_jobs = None)
    n_samples, n_features = int(random_state)

    n_jobs = len(n_jobs)
    num_components_2 = n_jobs
    # Pass 2.e-1 and n_jobs == n_jobs * n_jobs
    rng = n_jobs * n_jobs
    rng = n_jobs
    rng = n_jobs
    rng = n_jobs
    rng = n_jobs
    n_jobs = shuffle(n_jobs, n_jobs)
    rng = random_state.random_state((n_jobs=3, init=rand_jobs), random_state)

    random_state = random_state.normal(low=n_jobs, random_state)
    random_state = rng.integers(0)


    # make the random random features
    random_state = random_state.randint(batch
