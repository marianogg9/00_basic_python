numbers = [5, 7, 4, 2, 8, 3, 6, 1]

length_of_numbers = len(numbers)
iteration_count = 0

print(f"Original list: {numbers}")
print(">>>")

for k in range(1, length_of_numbers):
    for index in range(1, length_of_numbers):
        current_number = numbers[index]
        previous_number = numbers[index - 1]
        if previous_number > current_number:
            temp = numbers[index - 1]
            numbers[index - 1] = numbers[index]
            numbers[index] = temp
        print(str(numbers).replace(str(numbers[index]), "[" + str(numbers[index]) + "]"))
        iteration_count += 1  # Only there for iteration counting
    print("-" * 4)
print("<<<")
print(f"Final list: {numbers} found with {iteration_count} iterations")