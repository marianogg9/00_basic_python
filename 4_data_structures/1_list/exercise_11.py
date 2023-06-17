# TODO: Write a Python function
#       that takes two lists
#       and returns True if they have at least one common member
#       else False


def exercise_11(list1: list, list2: list) -> bool:
    if len(list1) == 0 or len(list2) == 0:
        return False
    else:
        tracker = dict()
        if len(list1) < len(list2):
            for i in list1:
                tracker[i] = 1
            for j in list2:
                if j in tracker:
                    return True
        else:
            for j in list2:
                tracker[j] = 1
            for i in list1:
                if i in tracker:
                    return True
    return False


# 1st test
list1 = ["train", "bike", "cat", "do", "I"]
list2 = []
assert exercise_11(list1, list2) is False

# 2nd test
list1 = ["train", "bike", "cat", "do", "I"]
list2 = ["cat"]
assert exercise_11(list1, list2) is True
