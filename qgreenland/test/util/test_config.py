import tempfile
from pathlib import Path

from qgreenland.util.config import (
    _deref_steps,
    _load_config,
)


MOCK_CONFIG = """
a: &ref-a
    foo: bar

b:
    <<: *ref-a
"""
MOCK_SCHEMA = """
a:
    foo: str()

b:
    foo: str()
"""

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


def test__load_config_copies_by_value():
    """Test that YAML references don't result in object copies by reference.

    We want to be able to use YAML anchors/references to DRY out the config, but
    also apply independent updates to those elements without affecting other
    elements.
    """
    with (
        tempfile.NamedTemporaryFile(mode='w') as conffile,
        tempfile.NamedTemporaryFile(mode='w') as schemafile,
    ):
        schemafile.write(MOCK_SCHEMA)
        schemafile.flush()
        conffile.write(MOCK_CONFIG)
        conffile.flush()

        cfg = _load_config(
            config_fp=Path(conffile.name),
            schema_fp=Path(schemafile.name),
        )
        assert id(cfg['a']) != id(cfg['b'])

        cfg['a']['foo'] = 'baz'
        assert cfg['a']['foo'] != cfg['b']['foo']
