"""Program 40: Find the greatest common divisor (GCD)."""

import math


def gcd(a, b):
    return math.gcd(a, b)


if __name__ == "__main__":
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("GCD:", gcd(a, b))