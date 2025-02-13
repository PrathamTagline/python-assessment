def remove_duplication_without_lossing_order(numberList):
    number_dictonary = {}
    without_duplication_list = []
    for number in numberList:
        if number in number_dictonary:
            number_dictonary[number] += 1
        else:
            number_dictonary[number] = 1

    for key in number_dictonary.keys():
        without_duplication_list.append(key)
    return without_duplication_list


list1 = [1, 2, 2, 3, 4, 5, 4, 5, 6]
print(remove_duplication_without_lossing_order(list1))
