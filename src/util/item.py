"""Food item information."""

from typing import TypedDict


class Item(TypedDict):
    """
    Stores information about a food item.
    """

    name: str
    store_name: str
    code: str | None
    price: int
    unit: str
    category: str
    quantity: int
    url: str
