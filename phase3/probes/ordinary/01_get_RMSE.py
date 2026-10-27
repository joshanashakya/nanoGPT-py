from optparse import OptionParser
import scipy as sp
from scipy import linalg, stats
import statsmodels.api as sm


def get_RMSE(true_params):
    """
    Gets the square error.
    """
