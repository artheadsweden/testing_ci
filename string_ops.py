def remove_vowels(word):
    vowels = "aeiouy"
    new_word = ""
    for character in word:
        if character.lower() not in vowels:
            new_word += character
    return new_word


def reverse_string(word):
    return word[::-1]


def translate_to_robber(text):
    vowels = "aeiouy"
    robber_str = ""

    for c in text:
        if c not in vowels and c.isalpha():
            robber_str += c + "o" + c
        else:
            robber_str += c

    return robber_str


def remove_consonant(word):
    vowels = "aeiouy"
    new_word = ""
    for character in word:
        if character.lower() in vowels:
            new_word += character
    return new_word


def main():
    print(remove_vowels("Hello"))
    print(reverse_string("Hello"))
    print(remove_consonant("Joakim"))


if __name__ == '__main__':
    main()
