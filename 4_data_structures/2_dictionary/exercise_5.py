# TODO: Write a Python program
#       to remove spaces from the keys of a dictionary.

dict1 = {
    " a": 1,
    "b b b": 2,
    "e  ": 3
}


def exercise_5(dict1):
    new_dict = dict()
    for i in dict1:
        new_dict[i.replace(" ","")] = dict1[i]
    return new_dict



assert exercise_5(dict1) == {"a": 1, "bbb": 2, "e": 3}