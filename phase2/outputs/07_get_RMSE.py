from optparse import OptionParser
import scipy as sp
from scipy import linalg, stats
import statsmodels.api as sm


def get_RMSE(results, true_params):
    """
    Gets the (normalized) root mean square error.
    """
    mod = RLM(results.endog, results.exog)
    res = mod.fit(results.params * 2, scale=1.5)
    print(res.params)
