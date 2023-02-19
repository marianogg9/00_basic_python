numbers = [2, 4, 6, 1, 8, 5, 3, 7]


def merge(left, right, array):

    # Get length of left
    left_length = len(left)
    # Get length of right
    right_length = len(right)

    i = 0
    j = 0
    k = 0

    while i < left_length and j < right_length:

        print(f"=====> Compare {left[i]} to {right[i]}")
        if left[i] <= right[j]:
            print(f"Put {left[i]} in index {k} of array: {array}")
            array[k] = left[i]
            i += 1
        else:
            print(f"Put {right[j]} in index {k} of array: {array}")
            array[k] = right[j]
            j += 1
        k += 1
    while i < left_length:
        array[k] = left[i]
        i += 1
        k += 1

    while j < right_length:
        array[k] = right[j]
        j += 1
        k += 1

    return array


def merge_sort(array):

    n = len(array)
    if n < 2:
        return

    mid = n // 2

    left = array[0: mid]
    right = array[mid: n]

    for i in range(0, mid):
        left[i] = array[i]

    for i in range(mid, n):
        right[i - mid] = array[i]

    merge_sort(left)
    merge_sort(right)

    # Merge two sorted parts of the array together
    merge(left, right, array)

    print(f"Output: {array}")


merge_sort(numbers)

# [2, 4, 1, 6, 8, 5, 3, 7]
# [2, 4, 1, 6]
# [2, 4]
# [2]
# [4]
# If right[j] > left[i]:
#    array[]
# [1. 6]
#