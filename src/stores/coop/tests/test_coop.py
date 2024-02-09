"""Coop store scraper tests."""

from src.stores.coop.coop import Coop


coop = Coop()


def test_get_categories_has_categories():
    """Test get_categories method returns something."""
    categories = coop._get_categories()
    assert isinstance(categories, dict)
    assert len(categories) > 0


def test_get_categories_has_known_categories_3_tests():
    """Test get_categories method returns known categories."""
    categories = coop._get_categories()

    known = {
        "Puu- ja köögiviljad": 1,
        "Pagaritooted": 47,
        "Piimatooted, munad, või": 20,
    }

    for name, _id in known.items():
        assert name in categories
        assert categories[name] == _id
