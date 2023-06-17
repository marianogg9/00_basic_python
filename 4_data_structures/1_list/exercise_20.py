# TODO: Write a Python program
#       to count integer in a given mixed list.


def exercise_20(list1: list) -> int:
    total = 0
    for i in list1:
        if type(i) == int:
            total += i
    return total


list1 = [1, 2, 'a', 'b', 50]

assert exercise_20(list1) == 53
