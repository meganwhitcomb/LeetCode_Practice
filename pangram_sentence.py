
"""
Given a string sentence containing only lowercase
English letters, return true if sentence is a pangram,
or false otherwise.
"""


import string

def check_if_pangram(sentence: str) -> bool:
    """
    Check if the Sentence is Pangram
    :param sentence:
    :return:
    """
    sentence.lower()
    alphabet = set(string.ascii_lowercase)
    for char in sentence:
        if char in alphabet:
            alphabet.remove(char)
    if not alphabet:
        return True
    return False

def main():

    print(check_if_pangram('tHequickbrownfOxjumpsoverthelazydog'))

if __name__ == '__main__':
    main()

# import string so we can use the set of all lowercase letters
# if char in ascii in sentence ascii[char] delete
