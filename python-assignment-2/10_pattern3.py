count = 1
for i in range(5):
    for j in range(i+1):
        print(f"{count}",end=" ")
        count += 1
    print("")