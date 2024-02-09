"""Coop store scraper tests."""

from src.stores.coop.coop import Coop
from src.util.item import Item


coop = Coop()


def test_get_items_has_items():
    """Test get_items method returns something."""
    items = coop.get_items()
    assert isinstance(items[0], Item)
    assert len(items) > 0
