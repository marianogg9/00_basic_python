# That's Halloween, and each kid collected candies in their bucket.
# Write a program returning a string telling which candy is the most popular
# The function should return a string including the most popular candy and the list of kids who have it.
from typing import List

kids_candies_bucket_report = [
    [1, 4, 5, 6, 2],  # Marty has those candies in his bag
    [2, 4, 5],  # Leon has those candies in his bag
    [6, 4, 2, 1],  # Anna has those candies in his bag
    [3, 2, 1]  # Mary has those candies in his bag
]


def exercise_5(report: List[List[int]]) -> str:
    helper = {}
    names = ['Marty','Leon','Anna','Mary']

    for i in kids_candies_bucket_report:
        for j in i:
            if j in helper:
                helper[j] += 1
            else:
                helper[j] = 1
        
    print(helper)

    mostCommon = max(helper,key=helper.get)

    firstLine = "Candy " + "\'" + str(mostCommon) + "\'" + " is the most popular.\n"
    kids, output = [], []
    for i in range(len(kids_candies_bucket_report)-1):
        if mostCommon in kids_candies_bucket_report[i]:
            kids.append(names[i])
    for kid in kids:
        output += str(kid)
        print(type(output))

    message = firstLine + output
    print(message)

    return message

assert exercise_5(kids_candies_bucket_report) == (
    "Candy '2' is the most popular. "
    "Marty, Leon, Anna and Mary picked it up"
)