"""Test client module."""

from math import prod
from src.db.client import get_supabase

client = get_supabase()


def test_get_products():
    """Test getting products."""
    products = client.from_("products").select("*").execute()

    if len(products.data) > 0:
        product = products.data[0]
        assert "id" in product
        assert "name" in product
        assert "store_name" in product
        assert "code" in product
