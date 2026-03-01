#! /usr/bin/env python3


import sys


def parse_args(args: list) -> dict:
    data = {}

    for arg in args:
        item, val = arg.split(":")
        data[item] = int(val)
    return data


def demo() -> None:
    print("=== Inventory System Analysis ===")

    items = parse_args(sys.argv[1:])
    all_count = sum(items.values())
    max_items = [item for item in items if items[item] == max(items.values())]
    min_items = [item for item in items if items[item] == min(items.values())]

    moderate = {item: items[item] for item in items if items[item] >= 4}
    scarce = {item: items[item] for item in items if items[item] < 4}

    restock_needed = {item for item in items if items[item] == 1}

    test_itm = "sword"

    print(f"Total items in inventory: {all_count}")
    print(f"Unique item types: {len(items)}")

    print("\n=== Current Inventory ===")
    for itm in items:
        print(f"{itm}: {items[itm]} units ({items[itm] * 100 / all_count}%)")

    print("\n=== Inventory Statistics ===")
    print(f"Most abundant: {max_items} ({items[max_items[0]]} unit)")
    print(f"Least abundant: {min_items} ({items[min_items[0]]} unit)")

    print("\n=== Item Categories ===")
    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}")

    print("\n=== Management Suggestions ===")
    print(f"Restock needed: {restock_needed}")

    print("\n=== Dictionary Properties Demo ===")
    print("Dictionary keys: ", end="")
    for key in items.keys():
        print(key, end=", ")

    print("\nDictionary values: ", end="")
    for value in items.values():
        print(value, end=", ")

    print(f"\nSample lookup - '{test_itm}' in inventory: {test_itm in items}")


if __name__ == "__main__":
    demo()
