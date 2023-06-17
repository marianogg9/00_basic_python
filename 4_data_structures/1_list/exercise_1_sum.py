# TODO: Write a Python program
#       to sum all the items in a list


def exercise_1(numbers: list) -> int:
    total = 0
    for i in numbers:
        total = total + i
    return total


numbers = [1, 2, 3, 4]

print(exercise_1(numbers) == 10)
assert sum == 10
