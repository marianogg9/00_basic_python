numbers = [1, 2, 60, 99, 201, 233, 300]

k = 99

half_list_index = len(numbers) // 2

number_found = False

while number_found is False:

    if k == numbers[half_list_index]:
        number_found = True
