def remove_vowels(word):
    vowels = "aeiouy"
    new_word = ""
    for character in word:
        if character.lower() not in vowels:
            new_word += character
    return new_word


def reverse_string(word):
    return word[::-1]


def main():
    print(remove_vowels("Hello"))
    print(reverse_string("Hello"))


if __name__ == '__main__':
    main()
