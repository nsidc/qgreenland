"""Test the three preferred forms of triple-quotation validate as expected."""
from qgreenland.models.config.dataset import DatasetMetadata

mock_meta = DatasetMetadata(
    title='mock',
    abstract='Mock.',
    citation={'text': 'mock', 'url': 'mock'},
)
expected = 'String content\n\nline 2\nmore.'


def test_indented_triple_quotes():
    actual = DatasetMetadata(**{
        **mock_meta.dict(),
        'abstract': (
            """String content

            line 2
            more."""
        ),
    }).abstract

    assert actual == expected


def test_unindented_triple_quotes():
    actual = DatasetMetadata(**{
        **mock_meta.dict(),
        'abstract': """
String content

line 2
more.""",
    }).abstract

    assert actual == expected


def test_weird_indented_triple_quotes():
    actual = DatasetMetadata(**{
        **mock_meta.dict(),
        'abstract': """String content

        line 2
        more.
        """,
    }).abstract

    assert actual == expected
