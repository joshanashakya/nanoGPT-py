from optparse import OptionParser
import scipy as sp
from scipy import linalg, stats
import statsmodels.api as sm


def get_RMSE(results, true_params):
    """
    Gets the (normalized) root mean square error.
    """
    diff = results.params.reshape(true_params.shape) - true_params
    raw_RMSE = sp.sqrt(((diff) ** 2).sum())
    param_norm = sp.sqrt((true_params**2).sum())
    return raw_RMSE / param_norm
