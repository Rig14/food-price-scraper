"""Test client module."""

from src.db.main import store_items
from src.util.item import Item


def test_store_items():
    """Test getting products."""
    products: list[Item] = [
        {
            "base_price": 100,
            "category": "electronics",
            "code": "123",
            "image": "https://example.com/image.jpg",
            "name": "Test Product",
            "price": 100,
            "quantity": 10,
            "store_name": "Test Store",
            "url": "https://example.com/product",
            "unit": "each",
        },
        {
            "base_price": 200,
            "category": "electronics",
            "code": "456",
            "image": "https://example.com/image.jpg",
            "name": "Test Product 2",
            "price": 200,
            "quantity": 20,
            "store_name": "Test Store",
            "url": "https://example.com/product",
            "unit": "each",
        },
    ]

    assert store_items(products) is True
