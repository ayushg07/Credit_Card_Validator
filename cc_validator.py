#Converts the input number into a list of digits
def intToArray(n):
    myArray = str(n)
    intArray = []
    for x in myArray:
        intArray.append(int(x))
    return intArray


#Adds digits of a two-digit number (e.g. 14 → 1 + 4 = 5)
def sumOfDigits(n):
    return (n // 10) + (n % 10)


#Doubles every second digit starting at 'startIndex'
#and replaces two-digit results with their digit sum
def oddEven(startIndex, intArray):
    for i in range(startIndex, len(intArray), 2):
        newDigit = intArray[i] * 2
        if newDigit < 10:
            intArray[i] = newDigit
        else:
            intArray[i] = sumOfDigits(newDigit)


#Main Luhn algorithm validation
def validate(n):
    intArray = intToArray(n)

    # Decide where to start doubling
    if len(intArray) % 2 == 0:
        oddEven(0, intArray)
    else:
        oddEven(1, intArray)

    # Check if total sum is divisible by 10
    if sum(intArray) % 10 == 0:
        return True
    else:
        return False


#User input and program output
print(validate(int(input("Enter CC number to validate:\n> "))))
