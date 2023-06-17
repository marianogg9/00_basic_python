# TODO: Write a Python program
#       to get the smallest number from a list.


def exercise_4(numbers: list) -> int:
    min_number = numbers[0]
    for i in numbers:
        if i <= min_number:
            min_number = i
    return min_number


numbers = [1, 2, 3, 4]
min_number = exercise_4(numbers)
print(min_number == 1)
assert min_number == 1
