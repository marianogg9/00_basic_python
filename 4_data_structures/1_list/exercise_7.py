# TODO: Write a Python program
#       to remove the duplicate in the list.


def exercise_7(sample_list: list) -> list:
    dictionary = dict()
    new_list = []
    for i in sample_list:
        if i not in dictionary:
            dictionary[i] = sample_list.index(i)
            new_list.append(i)
    return new_list


string_list = ['abc', 'xyz', 'abc', '1221']
assert exercise_7(string_list) == ['abc', 'xyz', '1221']