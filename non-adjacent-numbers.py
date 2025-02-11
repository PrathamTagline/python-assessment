list1 =[3, 2, 5, 10, 7]
sorted_list = sorted(list1,reverse=True)

highest_sum = 0

for index,value in enumerate(sorted_list):
    if index % 2 == 0:
        print(value)
        highest_sum += value 
        

print(highest_sum)