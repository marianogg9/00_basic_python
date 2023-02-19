numbers = [5, 7, 4, 2, 8, 3, 6, 1]

length_of_numbers = len(numbers)
iteration_count = 0

print(f"Original list: {numbers}")
print(">>>")

for k in range(0, length_of_numbers - 1):
    for index in range(0, length_of_numbers - 1 - k):
        current_number = numbers[index]
        next_number = numbers[index + 1]
        if current_number > next_number:
            temp = numbers[index + 1]
            numbers[index + 1] = numbers[index]
            numbers[index] = temp
        print(str(numbers).replace(str(numbers[index]), "[" + str(numbers[index]) + "]"))
        iteration_count += 1  # Only there for iteration counting
    print("-" * 4)
print("<<<")
print(f"Final list: {numbers} found with {iteration_count} iterations")