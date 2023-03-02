# TODO: Write a Python program to count the number of elements
#       which contains a string whose length is 2 or more
#       and the first and last character of that string are the same


def exercise_5(strings: list) -> int:
    return len([
        string for string in strings
        if len(string) >= 2 and string[0] == string[-1]
    ])


string_list = ['abc', 'xyz', 'aba', '1221']
assert exercise_5(string_list) == 2
