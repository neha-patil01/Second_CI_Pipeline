
def first_non_repeating_char(text):
    for char in text:
        if text.count(char) == 1:
            return char

    return None


if __name__ == "__main__":
    text = input("Enter a string: ")
    print(first_non_repeating_char(text))
