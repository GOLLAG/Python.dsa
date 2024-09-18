arr = [1, 4, 5]

def max(arr):
    M = arr[0]
    for num in arr:
        if num > M:
            M = num
    return M

print(max(arr))
REVERSE
arr = [1, 4, 5]

def reverse(arr):
    M = arr[::-1]
    return M

print(reverse(arr))
sort
def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

arr = [1, 2, 5]
print("Is the array sorted?:", is_sorted(arr))


SECOND LARGEST
arr = [1,5,3]
def sec(arr):
    arr.sort()
    return arr[1]
print(sec(arr))
Removing duplicates
arr = [1, 5, 3, 4, 5, 6, 3, 1, 4]

def dup(arr):
    uni = []  # Create an empty list to store unique elements
    
    # Iterate over each element in the array
    for elem in arr:
        # Check if the element is not already in the 'uni' list
        if elem not in uni:
            uni.append(elem)  # Add the element to 'uni' if it's not a duplicate
    
    return uni  # Return the list with unique elements

print(dup(arr))  # Call the function and print the result
3)
arr = [40,59,68,70]
M = 70
def no(arr,M):
    count = 0
    
    n = len(arr)
    for i in range(n):
        if arr[i]%5 == 0:
            count += 1
        
        elif arr[i] <= M:
            M -= arr[i]
            count += 1
            
    return count
print(no(arr,M))
