def to_absolute(number):
    """
    >>> to_absolute(3)
    3
    >>> to_absolute(-10)
    -10
    """
    if number <= 0:
        return -number
    return number # type: ignore