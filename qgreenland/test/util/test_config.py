from qgreenland.util.config import (
    _deref_steps,
)


MOCK_STEPS = [
    {'type': 'command', 'args': ['foo', 'bar']},
    {
        'type': 'template',
        'template_name': 'outer_template',
        'kwargs': {'wibble': 'wobble', 'biz': 'baz'},
    },
    {'type': 'command', 'args': ['banana', 'fanana']},
]
MOCK_TEMPLATES = {
    'outer_template': {
        'kwargs': ['wibble', 'biz'],
        'steps': [
            {
                'type': 'command',
                'args': ['this', 'struct', 'is', 'getting', 'deep!', 'biz {biz}'],
            },
            {
                'type': 'template',
                'template_name': 'inner_template',
                'kwargs': {
                    'wowie': 'zowie',
                    'oof': 'thathurts',
                    'wibble': '{wibble}',
                },
            },
        ],
    },
    'inner_template': {
        'kwargs': ['wowie', 'oof', 'wibble'],
        'steps': [
            {
                'type': 'command',
                'args': ['wowie {wowie}', 'oof {oof}', 'wibble {wibble}'],
            },
            {
                'type': 'command',
                'args': ['deeper', 'and', 'deeper'],
            },
        ],
    },


}
MOCK_RENDERED_STEPS = [
    {'type': 'command', 'args': ['foo', 'bar']},
    {
        'type': 'command',
        'args': ['this', 'struct', 'is', 'getting', 'deep!', 'biz baz'],
    },
    {
        'type': 'command',
        'args': ['wowie zowie', 'oof thathurts', 'wibble wobble'],
    },
    {
        'type': 'command',
        'args': ['deeper', 'and', 'deeper'],
    },
    {'type': 'command', 'args': ['banana', 'fanana']},
]


def test__deref_steps():
    expected = MOCK_RENDERED_STEPS
    actual = _deref_steps(
        MOCK_STEPS,
        templates=MOCK_TEMPLATES,
    )

    assert expected == actual
