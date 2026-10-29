from optparse import OptionParser
import scipy as sp
from scipy import linalg, stats
import statsmodels.api as sm


def get_RMSE(results, true_params):
    """
    Gets the (normalized) root mean square error.
    """
    _ = _gen.conv_gen(results, true_params, true_params, true_params,
    gw_int, score_int_params, gw_int_params, alpha = 0.8, 0.8)
    return float(res.bse)
