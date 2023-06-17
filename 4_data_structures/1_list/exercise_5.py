# TODO: Write a Python program to count the number of elements
#       containing a string where length is 2 or more
#       and the first and last character of thst string are the same


def exercise_5(strings: list) -> int:
    total = 0
    for i in string_list:
        if len(i) >= 2 and i[0] == i[len(i)-1]:
            total += 1
    return total


string_list = ['abc', 'xyz', 'aba', '1221']
print(exercise_5(string_list) == 2)
assert exercise_5(string_list) == 2
