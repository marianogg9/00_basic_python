numbers = [5, 7, 4, 2, 8, 3, 6, 1]

length_of_numbers = len(numbers)

print(f"Original list: {numbers}")
print(">>>")

for index in range(0, length_of_numbers - 1):
    current_number = numbers[index]
    next_number = numbers[index + 1]
    if current_number > next_number:
        temp = numbers[index + 1]
        numbers[index + 1] = numbers[index]
        numbers[index] = temp
    print(str(numbers).replace(str(numbers[index]), "[" + str(numbers[index]) + "]"))

print("<<<")
print(f"Final list: {numbers}")