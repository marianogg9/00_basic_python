# Write a program to return the only combination of numbers unique in the list
from typing import List, Tuple

big_list = [
    (1, 4, 5, 7, 4),
    (4, 5, 7, 1, 4),
    (2, 3, 6, 9, 5),
    (1, 2, 3, 4, 5),
    (2, 3, 5, 6, 9)
]


def exercise_7(big_list: List[Tuple[int]]) -> Tuple:
    # Your code here. Try to find at least two ways to do it.
    helper = []
    for i in big_list:
        helper.append(sorted(i))
    
    print(helper)

    for j in range(len(helper)-1):
        unique = True
        for k in helper[j+1:]:
            print('helper[j]: ',helper[j])
            print('k: ',k)
            if helper[j] == k:
                unique = False
                print(unique)
                break
        if unique:
            print(helper[j])
            return helper[j]


assert exercise_7(big_list) == (1, 2, 3, 4, 5)
