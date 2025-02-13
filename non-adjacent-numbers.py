def non_adjacent_sum(numberList):
    i = 0
    sum = 0
    taken_index = []
    while i != len(numberList) - 1:
        print(taken_index)
        if i == 0 or i == 1:
            if numberList[i] < numberList[i+1]:
                sum += numberList[i+1]
                taken_index.append(i+1)

                i += 3
                print(i)
            else:
                sum += numberList[i]
                taken_index.append(i)
                i += 2

        elif i > len(numberList) - 1:
            break

        elif i > 0:

            if i - 2 in taken_index:
                if not (i > len(numberList) - 2):
                    while  (numberList[i+1] > numberList[i]):
                        print("hellow")
                        if numberList[i] < numberList[i+1]:
                            sum += numberList[i+1]
                            taken_index.append(i+1)
                            i += 2
                            break
                        else:
                            i += 1

            elif  i - 2 not in taken_index:
                if numberList[i-1] > numberList[i]:
                    if numberList[i-1] > numberList[i+1]:
                        sum += numberList[i-1]
                        i += 1 
                elif numberList[i] > numberList[i-1]:
                    if numberList[i] > numberList[i+1]:
                        sum += numberList[i-1]
                        i += 2
                elif numberList[i+1] > numberList[i-1]:
                    if numberList[i+1] > numberList[i]:
                        sum += numberList[i-1]
                        i += 3

            
    return sum



list1 =[3, 2, 5, 10, 7]
print(non_adjacent_sum(list1))