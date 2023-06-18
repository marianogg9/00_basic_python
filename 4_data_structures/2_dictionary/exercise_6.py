# TODO: Write a Python program
#       to create a dictionary from two lists without losing duplicate values.

# Sample lists: ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII'], [1, 2, 2, 3]
# Expected Output: defaultdict(<class 'set'>, {'Class-V': {1}, 'Class-VI': {2}, 'Class-VII': {2}, 'Class-VIII': {3}})

list1 = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
list2 = [1, 2, 2, 3]


def exercise_6(first_list, second_list):
    # new_dict = dict(zip(first_list,second_list))
    new_dict = dict()
    
    for i in range(len(first_list)):
        new_dict.update({first_list[i]: second_list[i]})

    list_merged = list(zip(list1, list2))
    new_dict = {k:{v} for k,v in list_merged}
    print(list_merged)

    print(list_merged)
    return new_dict


assert exercise_6(list1, list2) == {'Class-V': {1}, 'Class-VI': {2}, 'Class-VII': {2}, 'Class-VIII': {3}}