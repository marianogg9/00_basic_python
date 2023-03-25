# TODO: Write a Python program
#       to filter even numbers from a given dictionary values.


def exercise_12(dict1):
    # Your code here
    return dict1


# 1st test
dict1 = {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
assert exercise_12(dict1) == {'V': [4, 6, 10], 'VI': [4, 12], 'VII': [8]}

# 2nd test
dict1 = {'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
assert exercise_12(dict1) == {'V': [], 'VI': [], 'VII': [2]}
