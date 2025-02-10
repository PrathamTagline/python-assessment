def flatten_list(tempList):
    flat_list = []
    temp = []
    for i in tempList:
        if isinstance(i ,list):
            flatten_list(i)
        else:
            flat_list.append(i)
    return flat_list


NumberList = [1,2,3,[4,[5,6,7],8],9]
print(flatten_list(NumberList))
