def swap(number1, number2):
    number1 = number1 + number2
    number2 = number1 - number2
    number1 = number1 - number2
    return (number1,number2)

print(swap(55,36))

