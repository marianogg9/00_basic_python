# TODO: Write a Python program
#       to check if a specific key "class" with value "V" exists
#       for each dictionary in a list


def exercise_13(list1):
    return [
        dictionary['class'] == "V"
        for dictionary in list1
    ]


# 1st test
list1 = [
    {'student_id': 1, 'name': 'Jean Castro', 'class': 'V'},
    {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'},
    {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'},
    {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'},
    {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'},
]
assert exercise_13(list1) == [
    True,
    True,
    False,
    False,
    False,
]
