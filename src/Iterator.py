from collections.abc import Iterable, Iterator
from typing import Any, List

from src.element import GameElement

class iteradorGE(Iterator):
    _position: int = None
    _reverse: bool = False

    def __init__(self, collection: List[Any]) -> None:
        self._collection = collection
        self._position = 0

    def __next__(self):
        """
        The __next__() method must return the next item in the sequence. On
        reaching the end, and in subsequent calls, it must raise StopIteration.
        """
        value = self._collection[self._position]
        self._position += 1

        return value

    def add_item(self, item: Any):
        self._collection.append(item)
