"""Program 38: Find the missing number using XOR."""

def missing_number(numbers):
    n = len(numbers)
    result = n

    for i, number in enumerate(numbers):
        result ^= i
        result ^= number

    return result


if __name__ == "__main__":
    numbers = list(map(
        int, input("Enter numbers separated by spaces: ").split()
    ))
    print("Missing number:", missing_number(numbers))