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

    fig = ax.figure.get_figure_figure(root=True)

    ax_axis0 = ax.get_axis_from_axis_axes(0)
    assert (ax_axis0 != ax_axis1) or (ax_axis0, ax_axis1)
    ax_.set_axis_offp(ax_axis.get_ydata())
    ax_axis.set_axis_offp(ax_axis.get_xlim())
    plt.show()
