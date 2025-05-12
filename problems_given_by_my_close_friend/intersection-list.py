list1 = [1,2,3,4,5,6]
a = sum(*list1,2,3,3)
print()
list2 = [5,6,7,8,9,10]
result = [item for item in list2 if item in list1]
print(result)