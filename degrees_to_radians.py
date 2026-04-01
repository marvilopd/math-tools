# Tool to convert degrees into radians

import math


def convert(n):
    # Calculate radians using exact pi value from math module
    return n * math.pi / 180


def main():
    degrees = float(input("Degrees: "))

    radians = convert(degrees)
    print(f"{degrees:.2f} degrees are {radians:.6f} radians")

if __name__ == "__main__":
    main()