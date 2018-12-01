def assert_array_equal(a, b, units_equal=True, **kwargs):
    """Assert pint arrays are equal

    :param a: first array to compare
    :param b: other array to compare
    :param units_equal: True to fail if units are not equal, False to pass as long as data is equal once converted to common units.
    :param **kwargs: kwargs to pass to ``np.testing.assert_array_equal``

    :raises AssertionError: the input arrays are not equal.
    """
    # TODO: decide whether to make this numpy dependent or not
    pass
