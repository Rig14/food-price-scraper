"""Coop Store scraper."""

from src.util.item import Item
from src.util.store import Store


class Coop(Store):
    """Coop Store class."""

    def __init__(self):
        self.name = "Coop"

    def get_items(self) -> list[Item]:
        """Returns all the food items that Coop web store has."""
        return [
            Item("Milk", "123", 199, "Dairy", 10),
        ]
