numbers = [1,2,3,4,5]
sum_first_last = numbers[0]  +numbers[-1]
numbers[0] = sum_first_last - numbers[0]
numbers[-1] = sum_first_last - numbers[-1]

print(numbers)