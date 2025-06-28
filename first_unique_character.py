"""
Given a string s, find the first non-repeating character
in it and return its index. If it does not exist, return -1.
"""


def first_uniq_char(s: str) -> int:
    """
    Prints index of first non-repeating character in given string.
    :param s:
    :return:
    """
    char_counts = {}
    for char in s:
        if not char in char_counts:
            char_counts[char] = 1
        else:
            char_counts[char] += 1

    for i, char in enumerate(s):  # Use enumerate here
        if char_counts[char] == 1:
            return i
    return -1


def main():

    print(first_uniq_char('aaabbbc'))

if __name__ == '__main__':
    main()
