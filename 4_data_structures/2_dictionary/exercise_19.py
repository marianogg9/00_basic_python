# TODO: Write a Python program
#       which update values for keys in a dictionary


def exercise_19(dict1):
    return dict1


dict1 = {
    "message": "hello", "username": "James"
}
assert exercise_19(dict1) == {"message": "Bonjour", "username": "Francois"}
assert id(exercise_19(dict1)) == id(dict1)
