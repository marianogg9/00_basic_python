# Write a Python program to remove an item from a set if it is present in the set.


def exercise_18():
    # Your code here
    return


basket = {"Hamburger", "Rice", "Carrot", "Eggs"}

item_to_remove = "Hamburger"
assert exercise_18(basket, item_to_remove) == {"Rice", "Carrot", "Eggs"}

item_to_remove = "Cauliflower"
assert exercise_18(basket, item_to_remove) == {"Rice", "Carrot", "Eggs"}