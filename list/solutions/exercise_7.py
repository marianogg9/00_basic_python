# TODO: Write a Python program
#       to remove the duplicate in the list.


def exercise_7(sample_list: list) -> list:
    sample_list.pop(2)
    return sample_list


string_list = ['abc', 'xyz', 'abc', '1221']
assert exercise_7(string_list) == ['abc', 'xyz', '1221']