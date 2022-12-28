"""Includes logic converting words into pig latin."""
import sys

vowels = ['a', 'e', 'i', 'o', 'u', 'y']


def main():
    """Return pig latin version of word until user interrupt."""
    print("Welcome to Pig Latin Maker.'\n")

    while True:

        user_word = input("\n\nEnter a word and press enter? (Enter 'n' to quit)\n ")
        if user_word.lower() == "n":
            break

        first_letter = user_word[0]
        suffix = first_letter + 'ay' if first_letter not in vowels else first_letter + 'way'
        pig_latin_word = user_word[1:] + suffix

        print("\n\n")
        print(pig_latin_word, file=sys.stderr)
        print("\n\n")

    input("\nPress Enter to exit.")


print(__name__)
if __name__ == "__main__":
    main()
