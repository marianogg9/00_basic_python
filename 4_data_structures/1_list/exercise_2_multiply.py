# TODO: Write a Python program
#       to multiply all the items in a list.


def exercise_2(numbers: list) -> int:
    total = numbers[0]
    for i in numbers[1:]:
        total = total * i
    return total

numbers = [1, 2, 3, 4]
total = exercise_2(numbers)
print(total == 24)
assert total == 24
