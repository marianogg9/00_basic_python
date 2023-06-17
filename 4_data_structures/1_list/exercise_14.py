# TODO: Write a Python program
#       to return a dictionary containing
#       the frequency of elements found in a list.


def exercise_14(list1: list) -> dict:
    tracker = dict()
    for i in list1:
        if i in tracker:
            tracker[i] += 1
        else:
            tracker[i] = 1
    return tracker


list1 = ["a", "a", "b", "b", "c", "d", "d", "d"]
assert exercise_14(list1) == {
    'a': 2,
    'b': 2,
    'c': 1,
    'd': 3
}
