# TODO: Write a Python program
#       to print the numbers of a specified list
#       after removing even numbers from it.


def exercise_13(list1: list) -> bool:
    new_list = []
    for i in list1:
        if i % 2 != 0:
            new_list.append(i)

    return new_list


list1 = [1, 2, 46, 7, 8, 9, 56]
assert exercise_13(list1) == [1, 7, 9]

list1 = [1, 78, 26, 7, 56, 27, 304]
assert exercise_13(list1) == [1, 7, 27]

list1 = [1, -78, 26, 7, -56, 27, -304]
assert exercise_13(list1) == [1, 7, 27]