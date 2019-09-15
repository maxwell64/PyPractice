import math

def digitSquaredSum(inp):

    inpSquaredSum = 0
    digits = str(inp)

    for i in digits:
        inpSquaredSum += int(i) ** 2

    return inpSquaredSum

print(digitSquaredSum(125))

def happyNumbers(inp):

    number = digitSquaredSum(inp)
    checked = []

    while number > 1 and number not in checked:
        checked.append(number)
        number = digitSquaredSum(number)

    return number == 1

def happyCheck(limit):

    happyList = []

    for i in range(limit):
        if happyNumbers(i) == True:
            happyList.append(i)

    print(happyList)

happyCheck(200000)