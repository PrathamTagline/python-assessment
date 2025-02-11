def non_adjacent_sum(numberList):
    sorted_list = sorted(numberList,reverse=True)
    highest_sum = 0

    for index,value in enumerate(sorted_list):
        if index % 2 == 0:
            highest_sum += value 
    return highest_sum        

list1 =[3, 2, 5, 10, 7]
print(non_adjacent_sum(list1))