"""Selver store scraper."""

import random
import time
import requests
from src.util.item import Item
from src.util.store import Store
from src.stores.selver.helper import construct_request


class Selver(Store):
    """Selver Store class."""

    def __init__(self):
        self.name = "Selver"

    def get_items(self, sleep: float = 1, _test: bool = False) -> list[Item]:
        """
        Returns all the food items Selver web store has.

        :param _test: bool: if True, the method will return a list of items for testing purposes (smaller request size)
        :param sleep: float: time to sleep between requests (seconds)
        """
        items: list[Item] = []
        category_ids = self._get_ids()

        # split category_ids into chunks of 3
        chunks = []
        for i in range(0, len(category_ids), 3):
            try:
                chunks.append(category_ids[i : i + 3])
            except IndexError:
                chunks.append(category_ids[i:])

        # if testing is enabled, only get one random chunk
        if _test:
            chunks = [chunks[random.randint(0, len(chunks) - 1)]]

        # get items from each chunk
        for chunk in chunks:
            time.sleep(sleep)
            items.extend(self._get_items_from_categories(chunk))

        return items

    def _get_ids(self) -> list[int]:
        """Get all category ids."""
        # Product categories API endpoint
        url = 'https://www.selver.ee/api/catalog/vue_storefront_catalog_et/category/_search?request={"query":{"bool":{"filter":{"bool":{"must":[{"terms":{"id":[3]}},{"terms":{"is_active":[true]}}]}}}}}&size=4000'

        response = requests.get(url)
        data = response.json()
        # find the base categories
        categories = data["hits"]["hits"][0]["_source"]["children_data"]
        # extract sub-categories
        sub_categories = [category["children_data"] for category in categories]
        # extract category ids
        category_ids = [[y["id"] for y in x] for x in sub_categories]
        # make the 2d list into a 1d list
        ids = []
        for i in category_ids:
            ids.extend(i)

        return ids

    def _get_items_from_categories(self, category_ids: list[int] | int) -> list[Item]:
        """Get all items from a category."""
        # construct the request json string
        request = construct_request(category_ids)
        # construct the url
        url = (
            "https://www.selver.ee/api/catalog/vue_storefront_catalog_et/product/_search?request="
            + request
            + "&size=1000"
        )

        response = requests.get(url)
        data = response.json()

        products = [x["_source"] for x in data["hits"]["hits"]]

        items: list[Item] = []
        for product in products:
            price = product["final_price_incl_tax"]
            base_price = product["unit_price"]
            quantity = price / base_price
            unit = (
                " ".join(
                    [
                        x
                        for x in product["product_volume"].split(" ")
                        if x.replace(",", ".").isdigit() is False
                    ]
                )
                if product["product_volume"]
                else "each"
            )

            item = Item(
                store_name=self.name,
                name=product["name"],
                code=product["product_main_ean"],
                price=price,
                unit=unit,
                category=product["category"][0]["name"],
                quantity=quantity,
                url="https://www.selver.ee/" + product["url_path"],
                base_price=base_price,
                image="https://www.selver.ee/img/50/50/resize" + product["image"],
            )
            items.append(item)

        return items
