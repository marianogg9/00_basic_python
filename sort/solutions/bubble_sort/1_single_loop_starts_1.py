numbers = [5, 7, 4, 2, 8, 3, 6, 1]

length_of_numbers = len(numbers)

print(f"Original list: {numbers}")
print(">>>")

for index, current_number in enumerate(numbers):
    previous_number = numbers[index - 1]
    if previous_number > current_number:
        temp = numbers[index - 1]
        numbers[index - 1] = numbers[index]
        numbers[index] = temp
    print(str(numbers).replace(str(numbers[index]), "[" + str(numbers[index]) + "]"))

print("<<<")
print(f"Final list: {numbers}")