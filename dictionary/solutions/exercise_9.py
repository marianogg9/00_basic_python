# TODO: Write a Python program
#       to create a list of dictionaries of dictionary of lists.


def exercise_9(dic1):
    science_values = dic1['Science']
    language_values = dic1['Language']

    output_list = []

    for science_value, language_value in zip(science_values, language_values):
        output_list.append({
            "Science": science_value,
            "Language": language_value
        })
    return output_list


dict1 = {
    'Science': [88, 89, 62, 95],
    'Language': [77, 78, 84, 80]
}

assert exercise_9(dict1) == [
    {'Science': 88, 'Language': 77},
    {'Science': 89, 'Language': 78},
    {'Science': 62, 'Language': 84},
    {'Science': 95, 'Language': 80}
]
