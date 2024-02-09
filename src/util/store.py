"""Store Abstract Class."""

from abc import ABC, abstractmethod

from .item import Item


class Store(ABC):
    """Store Abstract Class."""

    @abstractmethod
    def get_items(self) -> list[Item]:
        """Get all items in store."""
        raise NotImplementedError
