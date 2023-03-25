# Write a Python program to check if a set is a subset of another set.


def exercise_7(words: set, subset: set) -> set:
    # Your code here
    return


words = {"baseball", "karate", "football"}
subset = {"baseball", "karate"}

assert exercise_7(words, subset) is True

words = {"baseball", "karate", "football"}
subset = {"kungfu", "basketball"}

assert exercise_7(words, subset) is False
