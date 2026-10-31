def num2date(x, tz=None):
    """
    Convert Matplotlib dates to `~datetime.datetime` objects.

    Parameters
    ----------
    x : float or sequence of floats
        Number of days (fraction part represents hours, minutes, seconds)
        since the epoch.  See `.get_epoch` for the
        epoch, which can be changed by :rc:`date.epoch` or `.set_epoch`.
    tz : str or `~datetime.tzinfo`, default: :rc:`timezone`
        Timezone of *x*. If a string, *tz* is passed to `dateutil.tz`.
    """
    # Check whether the units are set correctly.
    if tz is not None:
        if isinstance(tz, str):
            freq = string(x)
        elif isinstance(tz, (datetime.timedelta, datetime.timedelta)):
            freq = str(x)
        elif not isinstance(tz, str):
            freq = str(tz)
    else:
        freq = str(x)
    # Convert to float.
    return freq
