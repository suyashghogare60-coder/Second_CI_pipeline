"""Program 37: Rotate a string by K positions."""

def rotate_string(text, k):
    if not text:
        return text

    k = k % len(text)

    if k == 0:
        return text

    return text[-k:] + text[:-k]


if __name__ == "__main__":
    text = input("Enter a string: ")
    k = int(input("Enter rotation count: "))
    print("Rotated string:", rotate_string(text, k))