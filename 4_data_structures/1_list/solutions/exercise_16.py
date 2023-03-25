# TODO: Write a Python program
#       to insert an element
#       before each element of a list.


def exercise_16(list1: list, element) -> list:
    for index in range(len(list1), 0, -1):
        list1.insert(index-1, element)
    return list1


list1 = [1, 2, 3, 4]
list2 = exercise_16(list1, '-')
assert list2 == ["-", 1, "-", 2, "-", 3, "-", 4]

list1 = [1, 2, 3]
list2 = exercise_16(list1, '*')
assert list2 == ["*", 1, "*", 2, "*", 3]