
"""
Given an integer num, return the number of digits in num that divide num.
An integer val divides nums if nums % val == 0.
"""

def count_digits(num: int) -> int:
    """
    Count the Digits That Divide a Number
    :param num:
    :return:
    """
    num_string = str(num)
    divisible_digits = 0
    for val in num_string:
        val = int(val)
        if val == 0:
            continue
        if num % val == 0:
            divisible_digits += 1
    return divisible_digits

def main():
    print(count_digits(202))

if __name__ == '__main__':
    main()

# Store integer as string
# Loop over each character in the string
# Make the character an integer
# If modulo is 0 then we increment the digit counter
