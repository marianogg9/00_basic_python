# Write a Python program to check if two given sets have no elements in common


def exercise_14(first_set: set, second_set: set) -> bool:
    # Your code here
    return


cars_1 = {"Ferrari", "Mercedes"}
cars_2 = {"Ferrari", "Mclaren"}

assert exercise_14(cars_1, cars_2) is False

cars_1 = {"Chevrolet", "Mercedes"}
cars_2 = {"Ferrari", "Mclaren"}

assert exercise_14(cars_1, cars_2) is True
