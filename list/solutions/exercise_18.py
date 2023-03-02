# TODO: Write a Python program
#       to generate all permutations of a list in Python.
from itertools import permutations


def exercise_18(list1: list) -> list:
    return list(permutations(list1, 3))


list1 = [1, 2, 3]
assert exercise_18(list1) == [
    (1, 2, 3),
    (1, 3, 2),
    (2, 1, 3),
    (2, 3, 1),
    (3, 1, 2),
    (3, 2, 1)
]
