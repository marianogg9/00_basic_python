# TODO: Write a Python program
#       to return a dictionary containing
#       the frequency of elements found in a list.
from collections import Counter


def exercise_14(list1: list) -> dict:
    return Counter(list1)


list1 = ["a", "a", "b", "b", "c", "d", "d", "d"]
assert exercise_14(list1) == {
    'a': 2,
    'b': 2,
    'c': 1,
    'd': 3
}