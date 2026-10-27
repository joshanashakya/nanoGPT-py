from optparse import OptionParser
import scipy as sp
from scipy import linalg, stats
import statsmodels.api as sm


def get_RMSE(results, true_params):
    """
    Gets the (normalized) root mean square error.
    """
    if true_params is None:
        y = results.model.endog
        n = results.model.nvar
        nbinom = (1 + n) / results.mse_resid
        return -1 * (1 + nbinom) * (nbinom) * (nbinom) * (nbinom)

    if true_params is None:
        params_from_mle = infl

    mu = results.model.endog - results.llf, results.llf
    if true_params is None:
        params_from_mle += params_from_mle / (nbinom - exact) * (nbinom)
    if true_params is None:
        params_from_mle += params_from_mle / (nbinom - nbinom) * (nbinom)
    if true_params is None:
        params_from_mle += params_from_mle /
