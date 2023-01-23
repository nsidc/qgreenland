from collections import Counter
from typing import Iterator


def find_duplicates(items: Iterator[str]) -> list[str]:
    return [i for i, count in Counter(items).items() if count > 1]
