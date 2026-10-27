"""Program 33: Find the first non-repeating character."""

def first_non_repeating(text):
    for char in text:
        if text.count(char) == 1:
            return char

    return None


if __name__ == "__main__":
    text = input("Enter a string: ")
    print("First non-repeating character:", first_non_repeating(text))