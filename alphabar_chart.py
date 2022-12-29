"""Implements bar chart for provided string."""


def parse_string_to_letter(parse_string: str) -> dict:
    """Return a dictionary with count of each letter in string."""
    r_dict = {}
    for letter in parse_string:
        cur_val = r_dict.get(letter)
        if cur_val:
            r_dict[letter] = cur_val + 1
        else:
            r_dict.update({letter: 1})
    if r_dict.get(' '): r_dict.pop(' ')

    return r_dict


def main():
    """Print bar chart of letters in user provided string ."""
    print("A string walks into a bar...'\n")

    user_input = input("\n\nEnter a string and press enter?\n")

    letter_dict = parse_string_to_letter(parse_string=user_input)

    print("\n\n")
    # print the bar chart
    #TODO: pprint & defaultdict exploration
    
    print("\n\n")

    input("\nPress Enter to exit.")


if __name__ == "__main__":
    main()
