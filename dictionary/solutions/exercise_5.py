# TODO: Write a Python program
#       to remove spaces from the keys of a dictionary.

dict1 = {
    " a": 1,
    "b b b": 2,
    "e  ": 3
}

def exercise_5(dict1):
    return {k.replace(" ", ""): v for k, v in dict1.items()}


assert exercise_5(dict1) == {"a": 1, "bbb": 2, "e": 3}