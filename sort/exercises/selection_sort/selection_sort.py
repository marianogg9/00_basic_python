# https://www.youtube.com/watch?v=GUDLRan2DWM

numbers = [5, 7, 4, 2, 8, 3, 6, 1]

for i in range(len(numbers)-2):
    x = numbers.index(min(numbers[i:]))
    y = numbers[i]
    numbers[i] = min(numbers[i:])
    numbers[x] = y
    print(numbers)