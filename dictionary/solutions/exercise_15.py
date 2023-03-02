# TODO: Write a Python program
#       to extract the list of values a dictionary
#       and returns values sorted in ascending order


def exercise_15(dict1):
    return dict1.values()


dict1 = {'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
assert exercise_15(dict1) == [19, 20, 21, 20]
