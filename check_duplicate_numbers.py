def duplicate_number(tempList):
    seen = set()
    duplicates = set()
    for i in tempList:
        if i in seen:
            duplicates.add(i)
        else:
            seen.add(i)

    return list(duplicates) if duplicates else "No duplicate numbers found."
    
numbers = [2, 4, 5, 2, 12, 44, 5, 1, 2, 3]

duplicate_numbers = duplicate_number(numbers)
print(duplicate_numbers)