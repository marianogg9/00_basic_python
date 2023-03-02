# TODO: Write a Python program
#       to remove duplicates from Dictionary.

dict1 = {
    ("1"): 2,
    ("2"): 2,
    ("3"): 4
}


def exercise_2(dict1):
    dico = {}

    for key, value in dict1.items():
        if value not in dico:
            dico[value] = [key]
        else:
            dico[value].append(key)

    for k, v in dico.items():
        if len(v) > 1:
            for vv in v:
                dict1.pop((vv))

    return dict1


assert exercise_2(dict1) == {("3"): 4}
