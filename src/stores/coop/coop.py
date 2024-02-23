"""Coop Store scraper."""

import json
import random
import time
import requests

from src.util.item import Item
from src.util.store import Store


class Coop(Store):
    """Coop Store class."""

    def __init__(self):
        self.name = "Coop"

    def get_items(
        self, sleep: float = 1, _test: bool = False, _log: bool = False
    ) -> list[Item]:
        """
        Returns all the food items Coop web store has.

        :param _test: bool: if True, the method will return a list of items for testing purposes (smaller request size)
        :param _log: bool: if True, the method will print the progress of the requests
        :param sleep: float: time to sleep between requests (seconds)
        """
        categories = self._get_categories()

        items = []

        if _test:
            # if testing only get items from 1 category
            random_key = list(categories.keys())[random.randint(0, len(categories) - 1)]
            value = categories[random_key]
            categories = {random_key: value}

        for idx, (category_name, category_id) in enumerate(categories.items()):
            time.sleep(sleep)
            if _log:
                print("[Coop]", f"{idx + 1} of {len(categories)} categories")
            items.extend(
                self._get_items_from_category(category_name, category_id, sleep=sleep)
            )

        return items

    def _get_categories(self) -> dict[str, int]:
        """Get category names and their respective ids."""
        url = "https://api.vandra.ecoop.ee/supermarket/categories/nested?language=et"

        response = requests.get(url)

        data = response.json().get("data")

        categories = {x["name"]: x["id"] for x in data}

        return categories

    def _get_items_from_category(
        self, category_name: str, category_id: int, sleep: float = 1
    ) -> list[Item]:
        """Get all items from a category."""
        page_url = f"https://api.vandra.ecoop.ee/supermarket/products?category={str(category_id)}&language=et&page="

        result: list[Item] = []
        # loop through all pages
        page_nr = 1
        while True:
            # request the page for products
            response = requests.get(page_url + str(page_nr))
            try:
                data = response.json().get("data")
                # if last page
                if not data:
                    break
            except json.JSONDecodeError:
                pass

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
            page_nr += 1

            time.sleep(sleep)

        return result
