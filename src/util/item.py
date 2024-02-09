"""Food item information."""


class Item:
    """
    Stores information about a food item.
    """

    def __init__(
        self,
        name: str,
        store_name: str,
        code: str | None,
        price: int,
        unit: str,
        category: str,
        quantity: int,
        url: str,
    ):
        self.name = name
        self.store_name = store_name
        self.code = code
        self.price = price
        self.unit = unit
        self.category = category
        self.quantity = quantity
        self.url = url

    def __repr__(self):
        return f"{self.store_name.capitalize()}(name:{self.name}, price:{self.price / 100}per, quantity:{self.quantity}/{self.unit}, {self.url})"

    def __str__(self):
        return (
            f"{self.name} {self.price / 100} per {self.quantity}/{self.unit} {self.url}"
        )
