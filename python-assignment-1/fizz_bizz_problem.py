def fizz_buzz(numberList):
    for i in numberList:
        if i % 3 == 0 and i % 5 == 0:
            print(f"{i} -> FizzBuzz")
        elif i % 3 == 0 and i % 5 != 0:
            print(f"{i} -> Fizz")
        elif i % 3 != 0 and i % 5 == 0:
            print(f"{i} -> Buzz")

    
numList = [number for number in range(1,101)]
fizz_buzz(numList)

