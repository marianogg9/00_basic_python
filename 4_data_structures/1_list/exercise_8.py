# TODO: Write a Python program
#       which returns if a list contains values or not.


def exercise_8(sample_list: list) -> bool:
    return len(sample_list) > 0


string_list = ['abc', 'xyz', 'abc', '1221']
assert exercise_8(string_list) is True
string_list = []
assert exercise_8(string_list) is False
