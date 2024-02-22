"""Coop store scraper tests."""

import random
import requests

from src.stores.coop.coop import Coop

#################################
# Setup
coop = Coop()
categories = coop._get_categories()
category_name, category_id = list(categories.items())[
    random.randint(0, len(categories) - 1)
]
items = coop._get_items_from_category(category_name, category_id)
#################################


def test_get_categories_has_categories():
    """Test get_categories method returns something."""
    assert isinstance(categories, dict)
    assert len(categories) > 0


def test_get_categories_has_known_categories_3_tests():
    """Test get_categories method returns known categories."""
    known = {
        "Puu- ja köögiviljad": 1,
        "Pagaritooted": 47,
        "Piimatooted, munad, või": 20,
    }

    for name, _id in known.items():
        assert name in categories
        assert categories[name] == _id


def test_get_items_from_category():
    """Test get_items_from_category method returns valid data."""
    assert len(items) > 0

    for item in items:
        assert item["name"] is not None
        assert item["price"] > 0
        assert item["unit"] is not None
        assert item["category"] == category_name
        assert item["quantity"] > 0
        assert item["url"] is not None
        assert item["base_price"] > 0
        assert item["image"] is not None

    # test that the url is valid for one of the items
    response = requests.get(items[0]["url"])
    assert response.status_code == 200


def test_all_categories_api_works():
    for category in categories.values():
        url = f"https://api.vandra.ecoop.ee/supermarket/products?category={str(category)}&language=et&page=1"
        response = requests.get(url)
        assert response.status_code == 200
        data = response.json().get("data")
        assert len(data) > 0


def test_item_image_link_works():
    test_items = items[:5]
    for i in test_items:
        url = i["image"]
        response = requests.get(url)
        assert response.status_code == 200
        assert response.headers["content-length"] is not None
        assert int(response.headers["content-length"]) > 0
