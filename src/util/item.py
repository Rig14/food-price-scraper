"""Food item information."""


class Item:
    """
    Stores information about a food item.
    """

    def __init__(self, name, code, price, category, quantity):
        self.name = name
        self.code = code
        self.price = price
        self.category = category
        self.quantity = quantity
