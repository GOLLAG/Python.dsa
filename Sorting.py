1) def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):  # Traverse through all elements in the array
        for j in range(0, n-i-1):  # Last i elements are already sorted
            if arr[j] > arr[j+1]:  # Swap if elements are in the wrong order
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
print("Sorted array:", bubble_sort(arr))
2) def sel(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):  # Find the minimum element in unsorted portion
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Swap the found minimum with the first element
    return arr
arr = [90,23,21,34]
print(sel(arr))
3) def linear_search(arr):
    n = len(arr)
    target = 13
    
    for i in range(n):
        if arr[i] == target:
           
            return i
    return -1


arr = [10,23,12,13]
print(linear_search(arr))
