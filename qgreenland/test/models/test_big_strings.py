"""Test the three preferred forms of triple-quotation validate as expected."""
from qgreenland.models.config.dataset import ConfigDatasetMetadata

mock_meta = ConfigDatasetMetadata(
    title='mock',
    abstract='mock.',
    citation={'text': 'mock', 'url': 'mock'},
)
expected = 'string content\n\nline 2\nmore.'


def test_indented_triple_quotes():
    actual = ConfigDatasetMetadata(**{
        **mock_meta.dict(),
        'abstract': (
            """string content

            line 2
            more."""
        ),
    }).abstract

    assert actual == expected


def test_unindented_triple_quotes():
    actual = ConfigDatasetMetadata(**{
        **mock_meta.dict(),
        'abstract': """
string content

line 2
more.""",
    }).abstract

    assert actual == expected


def test_weird_indented_triple_quotes():
    actual = ConfigDatasetMetadata(**{
        **mock_meta.dict(),
        'abstract': """string content

        line 2
        more.
        """,
    }).abstract

    assert actual == expected
