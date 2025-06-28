"""
Given an integer num, repeatedly add all its digits until
the result has only one digit, and return it.
"""


def add_digits(num: int) -> int:
    """
    Returns the sum of all its digits until the result has only one digit
    :param num:
    :return:
    """
    while num > 9:
        num = sum(int(digit) for digit in str(num))
    return num


def main():
    try:
        number_to_add = int(input('Input an integer: '))
        print(f'Adding the digits sums to {add_digits(number_to_add)}.')
    except ValueError:
        print('That\'s not an integer!')


if __name__ == '__main__':
    main()
