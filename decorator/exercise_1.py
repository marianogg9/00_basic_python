# Create a decorator which logs:
#   the name and parameter of any function decorated
#   the output

# 1 - Create a function taking a function as parameter and returns this function
# 2 - Since you want to modify add prints before after the execution of the function,
#   you need to define a function inside your current function, let's call it wrapper
#   this function parameters definition should match with parameters of your decorated functions
#   this function should return the same output that any decorated function
# 3 - For any decorated function, we want to get a similar result (nothing to add in function definition)

# function_name: hello_world
# Inputs: no params
# Processing ...
# Output: I say Hello World

# function_name: print_message
# Inputs: message='Bonjour a tous'
# Processing ... ...
# Output: User says `Bonjour a tous`

# function_name: sum_two_numbers
# Inputs: first_number=1, second_number=2
# Processing ... ... ...
# Output: 3

# Create your decorator here

# --------------------------


def hello_world():
    print("Processing ...")
    return "I say Hello World"


def print_message(message):
    print("Processing ... ...")
    return f"User says '{message}'"


def sum_two_numbers(first_number, second_number=0):
    print("Processing ... ... ...")
    return sum([first_number, second_number])


assert hello_world() == "I say Hello World"
assert print_message("Bonjour a tous") == "User says 'Bonjour a tous'"
assert sum_two_numbers(1, 2) == 3
