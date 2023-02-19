numbers = [5, 7, 4, 2, 8, 3, 6, 1]


def merge_sort(left, right, array):

    print(f"Left: {left}")
    print(f"Right: {right}")
    print(f"Array: {array}")

    # Get length of left
    left_length = len(left)
    # Get length of right
    right_length = len(right)

    i = 0
    j = 0
    k = 0

    while i < left_length and i < right_length:

        if left[i] > right[i]:
            array[i] = right[i]
            k += 1
            i += 1

        if right[i] >= left[i]:
            array[i] = left[i]
            k += 1
            j += 1

    while i < left_length:
        array[k] = left[i]
        i += 1
        k += 1

    while j < right_length:
        array[k] = right[j]
        j += 1
        k += 1

    return array


print(merge_sort(numbers[0:4], numbers[4:8], numbers))
