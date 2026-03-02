#! /usr/bin/env python3


import sys


def parse_args(args: list) -> dict:
    data = {}

    for arg in args:
        item, val = arg.split(":")
        data[item] = int(val)
    return data


def main() -> None:
    print("=== Inventory System Analysis ===")

    items = parse_args(sys.argv[1:])
    all_count = sum(items.values())
    max_items = [item for item in items if items[item] == max(items.values())]
    min_items = [item for item in items if items[item] == min(items.values())]

    min_items_count = items[max_items[0]] if len(max_items) else '0'
    max_items_count = items[min_items[0]] if len(min_items) else '0'

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
    print(f"Most abundant: {max_items} ({max_items_count} unit)")
    print(f"Least abundant: {min_items} ({min_items_count} unit)")

    print("\n=== Item Categories ===")
    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}")

    print("\n=== Management Suggestions ===")
    print(f"Restock needed: {restock_needed}")

    print("\n=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {list(set(items.keys()))}")
    print(f"Dictionary values: {list(set(items.values()))}")
    print(f"Sample lookup - '{test_itm}' in inventory: {test_itm in items}")


if __name__ == "__main__":
    main()
