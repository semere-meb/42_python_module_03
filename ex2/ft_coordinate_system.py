#! /usr/bin/env python3


import math


def distance(p1: tuple, p2: tuple) -> int:
    return math.sqrt(sum((p2[i] - p1[i]) ** 2 for i in [0, 1, 2]))


def parse_coordinate(arg: str) -> tuple:
    numbers_str = arg.split(",")
    numbers = []

    if len(numbers_str) != 3:
        print(f"Error: {arg} is and invalid coordinate")
        return None
    try:
        for num in numbers_str:
            numbers += [int(num)]
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: ValueError, Args: ({e})")
        return None
    else:
        return tuple(numbers)


def main() -> None:
    print("=== Game Coordinate System ===")
    p1: tuple = (0, 0, 0)

    p2: tuple = (10, 20, 5)
    print(f"\nPosition created: {p2}")
    if p2:
        print(f"Distance between {p2} and {p1}: {distance(p1, p2)}")

    val: str = "3,4,0"
    print(f'\nParsing coordinates: "{val}"')
    p2 = parse_coordinate(val)
    if p2:
        print(f"Distance between {p2} and {p1}: {distance(p1, p2)}")

    val = "abc,def,ghi"
    print(f'\nParsing invalid coordinates: "{val}"')
    p2 = parse_coordinate(val)
    if p2:
        print(f"Distance between {p2} and {p1}: {distance(p1, p2)}")

    cd: tuple = (3, 4, 0)
    print("\nUnpacking demonstartion:")
    print(f"Player at x={cd[0]}, y={cd[1]}, z={cd[2]}")
    x, y, z = cd
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    main()
