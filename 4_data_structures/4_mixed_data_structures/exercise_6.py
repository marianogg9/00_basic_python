def get_a_cat():
    return "I am a Cat"


def get_a_dog():
    return "I am a Dog"


def get_a_lion():
    return "I am a Lion"


def get_a_snake():
    return "I am a Snake"


def exercise_6(animal_to_select: str) -> str:
    # Your code here. Find at least two ways to solve the exercise
    message = ""
    if animal_to_select == "snake":
        message = get_a_snake()
    else: 
        if animal_to_select == "dog":
            message = get_a_dog()
        else:
            if animal_to_select == "cat":
                message = get_a_cat()
            else:
                message = get_a_lion()


    return message


assert exercise_6("snake") == "I am a Snake"
assert exercise_6("dog") == "I am a Dog"
assert exercise_6("cat") == "I am a Cat"
assert exercise_6("lion") == "I am a Lion"
