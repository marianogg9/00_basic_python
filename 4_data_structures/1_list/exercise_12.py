# TODO: Write a Python program
#       which removes the 0th, 4th and 5th elements of the list passed in input
#       and returns the same list updated

def exercise_12(list_colors: list) -> bool:
    list_colors.pop(0)  # pop 0th - now len(list_colors) = 5, 5th is 4th and 4th is 3rd
    list_colors.pop(3)  # pop new 3rd - now len(list_colors) = 4, 5th is 3rd and 4th is 2nd
    list_colors.pop(3)  # pop new 3rd
    return list_colors


list1 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

assert exercise_12(list1) == ['Green', 'White', 'Black']
