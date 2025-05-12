count = 1
for i in range(5):
    for j in range(i+1):
        if i == 2 or i == 3:
            if j == 0 or j == i:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        else:
            print("*",end=" ")
    print("")
