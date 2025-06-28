"""
Given an array of integers nums and an integer target, return indices
of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice.
"""
# With this number, what other number do I need to reach my target
# Have I seen this number before
# No? Store my current number
# Yes? This is my pair


def two_sum(nums: list[int], target: int):
    """
    Find the two numbers that sum to the target, return indices
    :param nums:
    :param target:
    :return:
    """
    past_numbers = {}
    for i, number in enumerate(nums):
        if target - number in past_numbers:
            return i, past_numbers[target - number]
        past_numbers[number] = i
    return None


def main():

    print(two_sum([2, 7, 11, 15], 9))


if __name__ == '__main__':
    main()
