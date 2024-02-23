"""Product data -> database."""

from src.db.client import get_supabase
from src.util.item import Item


def store_items(items: list[Item] | Item):
    """
    Stores specified items in the Supabase database.

    Args:
        items (list[Item] | Item): The items to be stored in the database. It can be a single item or a list of items.

    Returns:
        True if process suceeded
    """
    client = get_supabase()

    if not isinstance(items, list):
        items = [items]

    # put all items into the database
    try:
        client.from_("products").insert(items).execute()
        return True
    except Exception as e:
        return False
