# TODO: Write a Python program
#       to check that all values of a dictionary are the same.


def exercise_9(dict1):
    return all(val == 12 for val in dict1.values())


dict1 = {'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
assert exercise_9(dict1) is True

dict1 = {'Cierra Vega': 13, 'Alden Cantrell': 13, 'Kierra Gentry': 12, 'Pierre Cox': 12}
assert exercise_9(dict1) is False
