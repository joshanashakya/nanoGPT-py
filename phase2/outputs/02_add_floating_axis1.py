"""
===================
axis_direction demo
===================
"""

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.projections import PolarAxes
from matplotlib.transforms import Affine2D
import mpl_toolkits.axisartist as axisartist
from mpl_toolkits.axisartist import angle_helper, grid_finder
from mpl_toolkits.axisartist.grid_helper_curvelinear import GridHelperCurveLinear


def add_floating_axis1(ax):

    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    ax.set_title('Rotate')

    ax = fig.add_subplot(1, 2, 1)
    ax.set_aspect('equal')
    ax.set_alpha(0.15)

    ax.set_yscale('linear')

    ax.set_yscale('linear')

    ax.set_xscale('linear')
    ax.set_yscale('log')

    ax.set_yscale('log')

    ax.set_xlim(0, 2)
    ax.set_ylim(0, 1)
