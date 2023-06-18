# TODO: Write a Python program
#       to find the highest 3 keys of the dictionary.

dict1 = {1: 0, 2: 6, 3: 20, 9: 40}


def exercise_4(dict_input):
    return (list(dict_input.keys())[-3:])


assert set(exercise_4(dict1)) == set([9, 3, 2])
