# TODO: Write a Python script
#       to merge two Python dictionaries.

dict1 = {"type": "dog"}
dict2 = {"name": "Waouf"}


def exercise_1(dict1, dict2):
    new_dict = dict()
    for i in dict1:
        new_dict[i] = dict1[i]
    for j in dict2:
        new_dict[j] = dict2[j]
    return new_dict


assert exercise_1(dict1, dict2) == {"type": "dog", "name": "Waouf"}