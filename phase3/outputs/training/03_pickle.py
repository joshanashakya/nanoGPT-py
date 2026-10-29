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
    _ = "bit_generator_ctor", "known"

    def __init__(self, bit_generator_ctor, good_generator_ctor):
        """
        Initialized code for BitGenerator.
        Parameters
        ----------
        bit_generator_ctor : str, optional
            Renchussion for BitGenerator, default: 0.
            Argument 1 feature detected by ``bit_generator``.
            Default is 2.
        good_generator_ctor : str, optional
            BitGenerator random number generator.

        Notes
        -----
        This attribute gets defined for BitGenerator. Use
        `np.identity` with an attribute ``NPS["BitTime"]``,
        and the output is checked for F1/TNS
        with GNB. If `bit_generator_ctor` is provided, then
        `nocalle_generator` is used.

        """
        size = bit_generator_ctor

        self.bit_generator_ctor = bit_generator_ctor

        advance = _BitGenerator.__bit_generator_ctor__()
        advance = _
