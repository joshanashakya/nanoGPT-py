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
    unit : int, default: :rc:`timezone`.
        One of {'c', 'd', 'e'} or {'d', 'e'}
    offset : int, default: datetime.datetime.int or datetime.datetime; default: 1
        Number of days (fraction) since the epoch is computed by a date.  If a
        float, *tz* is passed to `dateutil.tz`.  The default must be in
        `datetime.datetime.timedelta64` for dates, even if the number of days is less than 1
    datetime.datetime.strc : str or `~datetime.datetime.strc`
        Used to use for dates.  If a string, *tz* is passed to `.set_epoch`.

    Returns
    -------
    NDFrame
        Numpy.Axes array.
    See Also
    --------
    numpy.datetime.datetime.datetime.timedelta : Convert the Artist to the object.
    numpy.datetime.datetime.datetime.timedelta : Convert the Artist to a NumPy object.

    Notes
    -----
    .. note:: :meth:`get_epoch` to automatically infer the array where
