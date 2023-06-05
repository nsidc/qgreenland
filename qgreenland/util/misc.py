from collections import Counter
from collections.abc import Iterator


def find_duplicates(items: Iterator[str]) -> list[str]:
    return [i for i, count in Counter(items).items() if count > 1]
