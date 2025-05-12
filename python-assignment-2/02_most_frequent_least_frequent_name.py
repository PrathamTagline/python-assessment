names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White']

def length_and_names_map_list1(nameList):
    length_name_map = {}
    for i in nameList:
        if len(i) not in length_name_map:
            length_name_map[len(i)] = [i]
        else:
            length_name_map[len(i)].append(i)
    return length_name_map

def most_frequent_names(lengthNameMap):
    most_frequent = sorted(lengthNameMap, key=lambda key: len(lengthNameMap[key]),reverse=True)
    for i in range(3):
        print(most_frequent[i],lengthNameMap[most_frequent[i]])


def least_frequent_names(lengthNameMap):
    most_frequent = sorted(lengthNameMap, key=lambda key: len(lengthNameMap[key]),reverse=False)
    for i in range(3):
        print(most_frequent[i],lengthNameMap[most_frequent[i]])

lenght_names_map = length_and_names_map_list1(names)


most_frequent_names(lenght_names_map)
print("")
least_frequent_names(lenght_names_map)

