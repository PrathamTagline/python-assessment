number_list = [1,2,3,4,5,6]

def list_sum(numberList):
    if len(numberList) == 1:
        return numberList[0]
    else:
        return numberList[0] + list_sum(numberList[1:])
    
print(list_sum(number_list))