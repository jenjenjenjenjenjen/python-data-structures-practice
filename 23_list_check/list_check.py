def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    for el in lst:
        x = isinstance(el, list)
        if x == False:
            return False
    return True
