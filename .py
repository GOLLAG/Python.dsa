arr = [1, 4, 5]

def max(arr):
    M = arr[0]
    for num in arr:
        if num > M:
            M = num
    return M

print(max(arr))
