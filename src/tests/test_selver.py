"""Test selver.py module."""

import json
import os
import random
import requests
from src.stores.selver.selver import Selver
from src.stores.selver.helper import construct_request

#########################
# Setup
selver = Selver()
category_ids = selver._get_ids()
products = selver._get_items_from_categories(category_ids[:6])
all_products = selver.get_items(_test=True)

#########################


def test_category_ids():
    """Test _get_ids method."""
    assert len(category_ids) > 0
    assert len(category_ids) == len(set(category_ids))


def test_construct_request():
    """Test if construct request helper function works."""
    assert (
        construct_request(209)
        == '{"query": {"bool": {"filter": {"bool": {"must": [{"terms": {"visibility": [2, 3, 4]}}, {"terms": {"status": [0, 1]}}, {"terms": {"category_ids": [209]}}]}}}}}'
    )


def test_request_categories():
    """Test if the request works for one category."""
    assert len(products) > 0
    for item in products:
        assert item["name"] is not None
        assert item["price"] > 0
        assert item["unit"] is not None
        assert item["quantity"] > 0
        assert item["url"] is not None
        assert item["base_price"] > 0
        assert item["image"] is not None


def test_item_links_work():
    """Test if the item links work. image and url"""
    item = products[0]
    response = requests.get(item["url"])
    assert response.status_code == 200
    response = requests.get(item["image"])
    assert response.status_code == 200

    item2 = products[random.randint(0, len(products))]
    response = requests.get(item2["url"])
    assert response.status_code == 200
    response = requests.get(item2["image"])
    assert response.status_code == 200


def test_get_all_products():
    assert len(all_products) > 0
    for item in all_products:
        assert item["name"] is not None
        assert item["price"] > 0
        assert item["unit"] is not None
        assert item["quantity"] > 0
        assert item["url"] is not None
        assert item["base_price"] > 0
        assert item["image"] is not None
    # log the products to a file for manual inspection
    path = os.path.join(os.path.dirname(__file__), "selver_products.json")
    with open(path, "w", encoding="UTF-8") as f:
        f.write(json.dumps(all_products, indent=4))
