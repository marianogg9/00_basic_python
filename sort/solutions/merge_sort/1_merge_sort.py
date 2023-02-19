numbers = [5, 7, 4, 2, 8, 3, 6, 1]


def merge_sort(left, right, array):

    # Get length of left
    left_length = len(left)
    # Get length of right
    right_length = len(right)

    i = 0

    while i < left_length and i < right_length:

        if left[i] > right[i]:
            array[i] = right[i]
        if right[i] > left[i]:
            array[i] = left[i]

        left_half = left_length // 2
        right_half = right_length // 2

        merge_sort(left[0: left_half], left[left_half: left_length], array)
        merge_sort(right[0: right_half], right[right_half: right_length], array)

        merge_sort(left, right, array)

        i += 1

    return array


print(merge_sort(numbers[0:4], numbers[4:8], numbers))