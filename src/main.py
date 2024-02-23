"""Scrape estonian food store prices."""

from src.db.main import store_items
from src.stores.coop.coop import Coop
from src.stores.selver.selver import Selver


def main():
    coop = Coop()
    selver = Selver()

    coop_items = coop.get_items(_log=True)
    store_items(coop_items)

    selver_items = selver.get_items(_log=True)
    store_items(selver_items)


if __name__ == "__main__":
    main()
