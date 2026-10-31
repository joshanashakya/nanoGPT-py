from __future__ import annotations

from collections.abc import Sequence
from typing import Literal, TypeAlias

from ._typing import Array, Device, DType, Namespace

_Norm: TypeAlias = Literal["backward", "ortho", "forward"]

# Note: NumPy fft functions improperly upcast float32 and complex64 to
# complex128, which is why we require wrapping them all here.

def fft(
    x: Array,
    /,
    xp: Namespace,
    *,
    n: int | None = None,
    axis: int = -1,
    norm: _Norm = "backward",
) -> Array:
    res = xp.fft.fft(x, n=n, axis=axis, norm=norm)
    if x.dtype in [xp.float32