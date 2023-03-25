# TODO: Write a Python program
#       to multiply all the items in a list.

from functools import reduce


def exercise_2(numbers: list) -> int:
    return reduce(lambda x, y: x * y, numbers)


numbers = [1, 2, 3, 4]
total = exercise_2(numbers)
assert total == 24
