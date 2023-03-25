# TODO: Write a Python program
#       to filter students depending on height and weight

dict1 = {
    'Cierra Vega': (6.2, 70),
    'Alden Cantrell': (5.9, 65),
    'Kierra Gentry': (5.8, 68),
    'Pierre Cox': (5.8, 66)
}


def exercise_18(dict1, height, weight):
    pass


assert set(exercise_18(dict1, 6.2, 70)) == set(["Cierra Vega"])
assert set(exercise_18(dict1, 5.8, 66)) == set(["Cierra Vega", "Pierre Cox"])
