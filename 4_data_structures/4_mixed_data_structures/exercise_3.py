# Find the sum of prices for cars in the list

# Filter cars whose prices >= 3000
from typing import List, Dict

cars = [
    {
        "brand": "Chevrolet",
        "model": "2016 Chevrolet Impala 2LT",
        "year": 2016,
        "mileage": "119862",
        "price": "$2500"
    },
    {
        "brand": "Chevrolet",
        "model": "2006 Honda CR-V EX",
        "year": 2006,
        "mileage": "117861",
        "price": "$9500"
    },
    {
        "brand": "Nissan",
        "model": "2013 Nissan Sentra FE+ SV",
        "year": 2013,
        "mileage": "62092",
        "price": "$3000"
    },
    {
        "brand": "Nissan",
        "model": "2011 Nissan Sentra 2.0 SR",
        "year": 2011,
        "mileage": "77868",
        "price": "$7999"
    },
    {
        "brand": "Jaguar",
        "model": "2000 Jaguar S-Type 4.0",
        "year": 2000,
        "mileage": "57010",
        "price": "$2995"
    }
]


def exercise_3(cars: List[Dict]) -> int:
    # Your code here, multiple options, try to find at least two different ways
    # Why way is the best? why?
    sum = 0
    for i in cars:
        sum = sum + int(i["price"][1:])
    return sum


assert exercise_3(cars) == 25994 # original 22999 is wrong, should be 25994
