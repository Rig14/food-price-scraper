"""Coop store scraper tests."""

import random
import requests

from src.stores.coop.coop import Coop


def test_get_categories_has_categories():
    """Test get_categories method returns something."""
    coop = Coop()
    categories = coop._get_categories()
    assert isinstance(categories, dict)
    assert len(categories) > 0


def test_get_categories_has_known_categories_3_tests():
    """Test get_categories method returns known categories."""
    coop = Coop()
    categories = coop._get_categories()
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
    coop = Coop()
    categories = coop._get_categories()
    category_name, category_id = list(categories.items())[
        random.randint(0, len(categories) - 1)
    ]
    items = coop._get_items_from_category(category_name, category_id)

    assert len(items) > 0
    print(items)
    for item in items:
        assert item["name"] is not None
        assert item["price"] > 0
        assert item["unit"] is not None
        assert item["category"] == category_name
        assert item["quantity"] > 0
        assert item["url"] is not None

    # test that the url is valid for one of the items
    response = requests.get(items[0]["url"])
    assert response.status_code == 200
