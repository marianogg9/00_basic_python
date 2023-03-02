# TODO: Write a Python program
#       to sort a list of dictionaries.
#       by qty


def exercise_17(list1: list) -> list:
    list1.sort(key=lambda elem: elem['qty'])
    return list1


list1 = [
    {"fruit": "Apple", "qty": 4},
    {"fruit": "Peach", "qty": 10},
    {"fruit": "Plum", "qty": 5},
    {"fruit": "Banana", "qty": 8},
]

assert exercise_17(list1)
assert id(exercise_17(list1)) == id(list1)