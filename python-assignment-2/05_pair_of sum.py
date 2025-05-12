list1=[1,2,3,4,5,6,7,8,9,10,5,10,7.5,7.5]
n = 15
pair = []
for index,i in enumerate(list1):
    for j in list1[index:]:
        if i + j == n:
            if ([j,i] not in pair) and ([i,j] not in pair):
                pair.append([i,j])

print(pair)


