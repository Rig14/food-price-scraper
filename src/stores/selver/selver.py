"""Selver store scraper."""

import requests
from src.util.item import Item
from src.util.store import Store

PRODUCT_URL = 'https://www.selver.ee/api/catalog/vue_storefront_catalog_et/product/_search?request={"query":{"bool":{"filter":{"bool":{"must":[{"terms":{"visibility":[2,3,4]}},{"terms":{"status":[0,1]}},{"terms":{"category_ids":[209,210,212,213,214,215,216,217,369]}}]}}}}}&size=24'


class Selver(Store):
    """Selver Store class."""

    def __init__(self):
        self.name = "Selver"

    def get_items(self) -> list[Item]:
        """Returns all the food items Selver web store has."""
        pass

    def _get_ids(self) -> list[int]:
        """Get all category ids."""
        # Product categories API endpoint
        url = 'https://www.selver.ee/api/catalog/vue_storefront_catalog_et/category/_search?request={"query":{"bool":{"filter":{"bool":{"must":[{"terms":{"id":[3]}},{"terms":{"is_active":[true]}}]}}}}}&size=4000'

        response = requests.get(url)
        data = response.json()
        # find the categories
        categories = data["hits"]["hits"][0]["_source"]["children_data"]
        # extract category ids from the categories
        ids = [category["id"] for category in categories]

        return ids
