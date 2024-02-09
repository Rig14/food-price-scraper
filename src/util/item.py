"""Food item information."""

from typing import TypedDict


class Item(TypedDict):
    """
    Stores information about a food item.
    """

    name: str
    store_name: str
    code: str | None
    price: float
    unit: str
    category: str
    quantity: float
    url: str
    image: str | None
    base_price: float
