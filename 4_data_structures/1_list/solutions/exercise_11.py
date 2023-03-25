# TODO: Write a Python function
#       that takes two lists
#       and returns True if they have at least one common member
#       else False


def exercise_11(list1: list, list2: list) -> bool:

    for w in list1:
        if w in list2:
            return True

    # reduce(lambda x,y: x or y, [True for w in list1 if w in list2 else False]])
    return False


# 1st test
list1 = ["train", "bike", "cat", "do", "I"]
list2 = []
assert exercise_11(list1, list2) is False

# 2nd test
list1 = ["train", "bike", "cat", "do", "I"]
list2 = ["cat"]
assert exercise_11(list1, list2) is True
