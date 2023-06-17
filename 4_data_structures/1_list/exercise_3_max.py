# TODO: Write a Python program
#       to get the largest number from a list.


def exercise_3(numbers: list) -> int:
    max = numbers[0]
    for i in numbers[1:]:
        if i >= max:
            max = i
    return max


numbers = [1, 2, 3, 4]
largest_number = exercise_3(numbers)
print(largest_number == 4)
assert largest_number == 4
