"""Coop Store scraper."""

import json
import requests

from src.util.item import Item
from src.util.store import Store


class Coop(Store):
    """Coop Store class."""

    def __init__(self):
        self.name = "Coop"

    def get_items(self, _test: bool = False) -> list[Item]:
        """
        Returns all the food items Coop web store has.

        :param _test: bool: if True, the method will return a list of items for testing purposes (smaller request size)
        """
        categories = self._get_categories()

        items = []

        # if testing only get items from 2 categories
        if _test:
            categories = dict(list(categories.items())[:2])

        for category_name, category_id in categories.items():
            items.extend(self._get_items_from_category(category_name, category_id))

        return items

    def _get_categories(self) -> dict[str, int]:
        """Get category names and their respective ids."""
        url = "https://api.vandra.ecoop.ee/supermarket/categories/nested?language=et"

        response = requests.get(url)

        data = response.json().get("data")

        # keep only categories that are below id 70 (only food categories)
        categories = {x["name"]: x["id"] for x in data if x["id"] < 70}

        return categories

    def _get_items_from_category(
        self, category_name: str, category_id: int
    ) -> list[Item]:
        """Get all items from a category."""
        url = f"https://api.vandra.ecoop.ee/supermarket/products?category={str(category_id)}&language=et&page="

        result: list[Item] = []
        # loop through all pages
        page_nr = 1
        while True:
            # request the page for products
            response = requests.get(url + str(page_nr))
            try:
                data = response.json().get("data")
            except json.JSONDecodeError:
                break

            for item in data:
                name = item["name"]
                code = None  # Coop does not have barcodes in their API
                price = item["price"]
                base_price = item["base_price"]
                quantity = price / base_price
                unit = item["base_unit"]
                url = f"https://vandra.ecoop.ee/et/toode/{item['id2']}-{item['slug']}"
                image = item["image"]
                result.append(
                    {
                        "name": name,
                        "store_name": self.name,
                        "code": code,
                        "price": price,
                        "unit": unit,
                        "category": category_name,
                        "quantity": quantity,
                        "url": url,
                        "base_price": base_price,
                        "image": image,
                    }
                )

            # if last page
            if not data:
                break

            page_nr += 1

        return result
