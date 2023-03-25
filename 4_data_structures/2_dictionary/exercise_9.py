# TODO: Write a Python program
#       to create a list of dictionaries of dictionary of lists.


def exercise_9():
    # Your code here
    pass


dict1 = {
    'Science': [88, 89, 62, 95],
    'Language': [77, 78, 84, 80]
}

assert exercise_9(dict1) == [
    {'Science': 88, 'Language': 77},
    {'Science': 89, 'Language': 78},
    {'Science': 62, 'Language': 84},
    {'Science': 95, 'Language': 80}
]