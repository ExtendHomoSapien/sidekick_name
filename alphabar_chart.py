"""Implements bar chart for provided string."""
import pprint
import collections
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

def make_dd_list(letter_dict: dict) -> collections.defaultdict:
    r_dict = collections.defaultdict(list)
    for k,v in letter_dict.items():
        for i in range(0,v):
            r_dict[k].append(k)
    return r_dict

def main():
    pp = pprint.PrettyPrinter()
    """Print bar chart of letters in user provided string ."""
    print("A string walks into a bar...'\n")

    user_input = input("\n\nEnter a string and press enter?\n")

    letter_dict = parse_string_to_letter(parse_string=user_input)

    print("\n\n")
    pp.pprint(make_dd_list(letter_dict))
    print("\n\n")

    input("\nPress Enter to exit.")


if __name__ == "__main__":
    main()
