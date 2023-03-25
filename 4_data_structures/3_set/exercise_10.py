# Write a Python program to use of frozensets


def exercise_10(animals: list) -> frozenset:
    # Your code here
    return


animals = ["Fox", "Cat", "Dog"]

assert type(exercise_10(animals)) == frozenset
assert exercise_10(animals) == {"Cat", "Dog", "Fox"}
assert exercise_10(animals) == {"Dog", "Fox", "Cat"}
assert exercise_10(animals) == {"Fox", "Cat", "Dog"}


