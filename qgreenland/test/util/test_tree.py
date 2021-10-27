from functools import partial

from qgreenland.util.tree import _matches_filters


SELECT_MANY_PATTERNS = ('*machine*', 'backgr*')
SELECT_ONE_PATTERNS = ('bedmachine_thickness',)


def test__matches_filters_no_patterns(layer_cfgs):
    test_func = partial(
        _matches_filters,
        include_patterns=(),
        exclude_patterns=(),
    )
    actual = [test_func(i) for i in layer_cfgs]
    expected = [True] * len(layer_cfgs)

    assert actual == expected


def test__matches_filter_specific_include_general_exclude(layer_cfgs):
    """Test that the "specific include" case works as expected.

    Under our current business logic, this is the fortunate case. The user
    clearly wanted to select the inverse of the "exclusion" set and add the
    "inclusion" set to that. This is what occurs.
    """
    test_func = partial(
        _matches_filters,
        include_patterns=SELECT_ONE_PATTERNS,
        exclude_patterns=SELECT_MANY_PATTERNS,
    )
    actual = [test_func(i) for i in layer_cfgs]
    expected = [False, True, False, True, True, True]

    assert actual == expected


def test__matches_filters_general_include_specific_exclude(layer_cfgs):
    """Test that the "specific exclude" case works as expected.

    Under our current business logic, this is the unfortunate case. The user
    clearly wanted to select the "inclusion" set and subtract the "exclusion"
    set from that. Instead they receive the full set.
    """
    test_func = partial(
        _matches_filters,
        include_patterns=SELECT_MANY_PATTERNS,
        exclude_patterns=SELECT_ONE_PATTERNS,
    )
    actual = [test_func(i) for i in layer_cfgs]
    expected = [True] * len(layer_cfgs)

    assert actual == expected


def test__matches_filters_include_only(layer_cfgs):
    test_func = partial(
        _matches_filters,
        include_patterns=SELECT_MANY_PATTERNS,
        exclude_patterns=(),
    )

    actual = [test_func(i) for i in layer_cfgs]
    expected = [True, True, True, False, False, False]

    assert actual == expected


def test__matches_filters_exclude_only(layer_cfgs):
    test_func = partial(
        _matches_filters,
        include_patterns=(),
        exclude_patterns=SELECT_ONE_PATTERNS,
    )
    actual = [test_func(i) for i in layer_cfgs]
    expected = [True, False, True, True, True, True]

    assert actual == expected
