# TODO: Write a Python program
#       which deletes the first 3 elements of a list
#       and returns the same list updated


def exercise_6(list1):
    for i in range(3):
        list1.pop(0)
    return list1

# 1st test
list1 = [1, 2, 3, 5, 6]
assert exercise_6(list1) == [5, 6]
assert id(exercise_6(list1)) == id(list1)
