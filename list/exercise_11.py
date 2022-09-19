# Write a Python function that takes two lists and returns True if they have at least one common member.


def exercise_11(list1: list, list2: list) -> bool:
    # Your code here
    return


list1 = ["train", "bike", "cat", "do", "I"]
list2 = []

assert exercise_11(list1, list2) is False

list1 = ["train", "bike", "cat", "do", "I"]
list2 = ["cat"]

assert exercise_11(list1, list2) is True
