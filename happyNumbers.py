def digitSquaredSum(inp):
    #returns the sum of all the digits in the input squared

    inpSquaredSum = 0
    digits = str(inp)

    for i in digits:
        inpSquaredSum += int(i) ** 2

    return inpSquaredSum

def happyNumbers(inp):
    #determines if the input is a happy number

    number = digitSquaredSum(inp)
    checked = []

    while number > 1 and number not in checked:
        checked.append(number)
        number = digitSquaredSum(number)

    return number == 1

def happyCheck(limit):
    #prints a list of the happy numbers up to the given limit

    happyList = []

    for i in range(limit):
        if happyNumbers(i) == True:
            happyList.append(i)

    print(happyList)

happyCheck(200000)