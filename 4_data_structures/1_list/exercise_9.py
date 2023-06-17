# TODO: Write a Python program
#       to clone or copy a list


def exercise_9(sample_list: list) -> bool:
    new_list = sample_list.copy()
    return new_list


string_list = ['abc', 'xyz', 'abc', '1221']
assert exercise_9(string_list) is not string_list
assert exercise_9(string_list) == string_list