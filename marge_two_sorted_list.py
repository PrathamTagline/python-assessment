def single_sorted_list(list1,list2):
    i,j = 0,0
    new_sorted_list = []
    while i != len(list1) +1  and  j != len(list2) + 1 :

        if i == len(list1)  and j != len(list2):
            new_sorted_list.extend(list2[j:])
            break

        elif i != len(list1)  and j == len(list2) :
            new_sorted_list.extend(list1[i:])
            break

        elif list1[i] == list2[j]:
            new_sorted_list.append(list1[i])
            new_sorted_list.append(list2[j])
            if i == len(list1) :
                j = len(list2) 
            elif j == len(list2) :
                i = len(list1) 
                i += 1 
            else:
                i += 1
                j += 1

        elif list1[i] > list2[j]:
            new_sorted_list.append(list2[j])
            j += 1
        elif list1[i] < list2[j]:
            new_sorted_list.append(list1[i])
            i += 1
    return new_sorted_list

sorted_list_1 = [1,4,5,6,7]
sorted_list_2 = [1,2,3,5,8,9,11]

print(single_sorted_list(sorted_list_1,sorted_list_2))