# Write a Python program to check if a given value is present in a set or not


def exercise_13(word_to_find: str, basket: set) -> bool:
    # Your code here
    return


basket = {"Pizza", "Cheese", "Cucumber", "Potato"}

word_to_find = "Potato"
assert exercise_13(word_to_find, basket) is True

word_to_find = "Patato"
assert exercise_13(word_to_find, basket) is False
