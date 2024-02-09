"""Coop Store scraper."""

import requests

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

    def _get_categories(self) -> dict[str, int]:
        """Get category names and their respective ids."""
        url = "https://api.vandra.ecoop.ee/supermarket/categories/nested?language=et"

        response = requests.get(url)

        data = response.json().get("data")

        # keep only categories that are below id 70 (only food categories)
        categories = {x["name"]: x["id"] for x in data if x["id"] < 70}

        return categories
