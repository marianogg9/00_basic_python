# TODO: Write a Python program
#       which returns a list of numbers
#       after removing even numbers to it.


def exercise_13(list1: list) -> bool:
    return [
        number for number in list1
        if number % 2 > 0
    ]


list1 = [1, 2, 46, 7, 8, 9, 56]
assert exercise_13(list1) == [1, 7, 9]

list1 = [1, 78, 26, 7, 56, 27, 304]
assert exercise_13(list1) == [1, 7, 27]

list1 = [1, -78, 26, 7, -56, 27, -304]
assert exercise_13(list1) == [1, 7, 27]