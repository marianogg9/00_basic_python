# TODO: Write a Python program
#       to convert a given dictionary into a list of tuples.


def exercise_11(dict1):
    return dict1.items()


# 1st test
dict1 = {
    1: 'red',
    2: 'green',
    3: 'black',
    4: 'white',
    5: 'black'
}
assert list(exercise_11(dict1)) == [
    (1, 'red'),
    (2, 'green'),
    (3, 'black'),
    (4, 'white'),
    (5, 'black')
]


# 2nd test
dict1 = {
    '1': 'Austin Little',
    '2': 'Natasha Howard',
    '3': 'Alfred Mullins',
    '4': 'Jamie Rowe'
}
assert list(exercise_11(dict1)) == [
    ('1', 'Austin Little'),
    ('2', 'Natasha Howard'),
    ('3', 'Alfred Mullins'),
    ('4', 'Jamie Rowe')
]