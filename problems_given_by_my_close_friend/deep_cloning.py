def deep_cloning(tempList):
    cloning_list = []
    for item in tempList:
        if isinstance(item,list):
            cloning_list.append(deep_cloning(item))
        else : 
            cloning_list.append(item)

    return cloning_list



original = [1,2,3,[4,[5,6,7],8],9]
clone_list =  deep_cloning(original)


clone_list[3][1][0] = 99

print(original)
print(clone_list)


