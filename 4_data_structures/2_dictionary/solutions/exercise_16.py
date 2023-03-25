# TODO: Write a Python program
#       to convert given a dictionary to a list of list.


def exercise_16(dict1):
    return [list(pair) for pair in dict1.items()]


dict1 = {'Red': 1, 'Green': 3, 'White': 5, 'Black': 2, 'Pink': 4}
assert exercise_16(dict1) == [
    ['Red', 1],
    ['Green', 3],
    ['White', 5],
    ['Black', 2],
    ['Pink', 4]
]
