# TODO: Write a Python program
#       to print all unique values in a dictionary.

dict1 = {
    1: 3,
    2: 3,
    4: 70,
    67: 9888
}


def exercise_3(dict1):
    new_dict = dict()
    for i in dict1:
        if dict1[i] not in new_dict.values():
            new_dict[i] = dict1[i]
    return list(new_dict.values())


assert exercise_3(dict1) == [3, 70, 9888]
