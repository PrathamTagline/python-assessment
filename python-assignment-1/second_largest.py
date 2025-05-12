def second_largest_numbrer(numberList):
    sorted_list = sorted(numberList,reverse=True)
    return sorted_list[1]

print(second_largest_numbrer([1,2,3,4,5,6,7]))
