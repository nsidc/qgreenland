from functools import partial

from qgreenland.util.tree import _matches_filters


CANDIDATE_STRINGS = [
    'bedmachine_error',
    'bedmachine_thickness',
    'background',
    'lat_0_25_deg',
    'lon_0_5_deg',
    'lon_5_deg',
]
SELECT_MANY_PATTERNS = ('*machine*', 'backgr*')
SELECT_ONE_PATTERNS = ('bedmachine_thickness',)


def test__matches_filters_no_patterns():
    test_func = partial(
        _matches_filters,
        include_patterns=(),
        exclude_patterns=(),
    )
    actual = [test_func(i) for i in CANDIDATE_STRINGS]
    expected = [True] * len(CANDIDATE_STRINGS) 

    assert actual == expected


def test__matches_filter_specific_include_general_exclude():
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
    actual = [test_func(i) for i in CANDIDATE_STRINGS]
    expected = [False, True, False, True, True, True]

    assert actual == expected


def test__matches_filters_general_include_specific_exclude():
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
    actual = [test_func(i) for i in CANDIDATE_STRINGS]
    expected = [True] * len(CANDIDATE_STRINGS)

    assert actual == expected


def test__matches_filters_include_only():
    test_func = partial(
        _matches_filters,
        include_patterns=SELECT_MANY_PATTERNS,
        exclude_patterns=(),
    )

    actual = [test_func(i) for i in CANDIDATE_STRINGS]
    expected = [True, True, True, False, False, False]

    assert actual == expected


def test__matches_filters_exclude_only():
    test_func = partial(
        _matches_filters,
        include_patterns=(),
        exclude_patterns=SELECT_ONE_PATTERNS,
    )
    actual = [test_func(i) for i in CANDIDATE_STRINGS]
    expected = [True, False, True, True, True, True]

    assert actual == expected
