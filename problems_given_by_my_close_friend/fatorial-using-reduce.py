from functools import reduce
no = 5
numbers = [i for i in range(1,no+1)]
result = reduce(lambda x,y : x*y,numbers)
print(result)


