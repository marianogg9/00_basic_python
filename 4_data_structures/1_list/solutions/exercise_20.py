# TODO: Write a Python program
#       to count integer in a given mixed list.


def exercise_20(list1: list) -> int:
    return sum([element for element in list1 if isinstance(element, int)])


list1 = [1, 2, 'a', 'b', 50]

assert exercise_20(list1) == 53
