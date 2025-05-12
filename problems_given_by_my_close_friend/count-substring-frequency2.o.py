str1 = "ABABBABABABA"
substring = "ABA"
i,j = 0,0
count = 0

while i != len(str1) - 1:
    if str1[i] == substring[j]:
        j += 1
        if (j) % len(substring) != 0:
            i += 1

        else:
            j = 0
            count += 1 
    
    else:
        i += 1
        j = 0

print(count)









