# TODO: Write a Python program
#       to update elements in list stored as dictionary values.


def exercise_10():
    # Your code here
    pass


dict1 = {
    'Math': [88, 89, 90],
    'Physics': [92, 94, 89],
    'Chemistry': [90, 87, 93]
}

assert exercise_10(dict1) == {
    'Math': [89, 90, 91],
    'Physics': [90, 92, 87],
    'Chemistry': [90, 87, 93]
}