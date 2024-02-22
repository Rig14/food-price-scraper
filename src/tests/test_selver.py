"""Test selver.py module."""

from src.stores.selver.selver import Selver
from src.stores.selver.helper import construct_request

#########################
# Setup
Selver = Selver()
category_ids = Selver._get_ids()

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
