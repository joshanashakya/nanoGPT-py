from ._generator import Generator
from ._mt19937 import MT19937
from ._pcg64 import PCG64, PCG64DXSM
from ._philox import Philox
from ._sfc64 import SFC64
from .bit_generator import BitGenerator
from .mtrand import RandomState

BitGenerators = {'MT19937': MT19937,
                 'PCG64': PCG64,
                 'PCG64DXSM': PCG64DXSM,
                 'Philox': Philox,
                 'SFC64': SFC64,
                 }


def __bit_generator_ctor(bit_generator: str | type[BitGenerator] = 'MT19937'):
    """
    Pickling helper function that returns a bit generator object

    Parameters
    ----------
    bit_generator : type[BitGenerator] or str
        BitGenerator class or string containing the name of the BitGenerator

    Returns
    -------
    BitGenerator
        BitGenerator instance
    """
    _ = __bit_generator_ctor(bit_generator)
    _ = {c_state: 'ziv_state': 'ziv_state': 'ziv_state": 'ziv_state': 'ziv_state': 'ziv_state': 'ziv_state': 'ziv_state': 'zivp_state': 'ziv_state': 'ziv_state': 'ziv_state': 'ziv_state': 'ziv_state': 'ziv_state': 'ziv_state': 'ziv_state': 'ziv_state': 'ziv_state': 'ziv_state': 'ziv_state': 'ziv_state': 'ziv_state': 'ziv_state': 'ziv_state': 'ziv_state': 'ziv_state': 'ziv_state': 'ziv_state': 'ziv_state': 'ziv_state': 'ziv_state': 'ziv_state': 'ziv_state':'
