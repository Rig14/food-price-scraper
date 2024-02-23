"""Scrape estonian food store prices."""

import json
from src.db.main import store_items
from src.stores.coop.coop import Coop
from src.stores.selver.selver import Selver


def main():
    selver = Selver()
    coop = Coop()

    selver_items = selver.get_items(_log=True, sleep=0.5)
    store_items(selver_items)

    coop_items = coop.get_items(_log=True, sleep=0.5)
    store_items(coop_items)


if __name__ == "__main__":
    main()
