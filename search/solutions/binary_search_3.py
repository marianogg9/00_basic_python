numbers = [1, 2, 60, 99, 201, 233, 300]

k = 300

number_found = False

start_index = 0
end_index = len(numbers)

while number_found is False:

    half_list_index = (start_index + end_index) // 2
    print(f"Is {k} lower than or equal to {numbers[half_list_index]}?")
    if k == numbers[half_list_index]:
        number_found = True
        print(f"Number: {k  } found at index {half_list_index}")
    elif k > numbers[half_list_index]:
        print(f"Keep right side")
        start_index += 1
