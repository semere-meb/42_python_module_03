import sys


def parse_args() -> None:
    print("=== Command Quest ===")

    if len(sys.argv) == 1:
        print("No arguments provided!")
    print(f"Program name: {sys.argv[0]}")

    length = len(sys.argv)
    if length > 1:
        print(f"Arguments received: {length - 1}")
    i: int = 1
    while i < length:
        print(f"Argument {i}: {sys.argv[i]}")
        i += 1
    print(f"Total arguments: {length}")


if __name__ == "__main__":
    parse_args()
