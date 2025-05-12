def buuble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

numberlist = [64, 34, 25, 12, 22, 11, 90]
print("Original list:", numberlist)
print("Bubble sort:", buuble_sort(numberlist))  
print("Selection sort:", selection_sort(numberlist))

