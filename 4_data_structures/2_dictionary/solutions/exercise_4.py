# TODO: Write a Python program
#       to find the highest 3 keys of the dictionary.

dict1 = {1: 0, 2: 6, 3: 20, 9: 40}


def exercise_4(dict_input):

    highest_keys = list(sorted(dict_input.keys(), reverse=True))[0:3]
    print(highest_keys)


exercise_4(dict1)