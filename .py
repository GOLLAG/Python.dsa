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
4) def pal(str,f,s):
    for i in range(f,s+1):
        if str(i) == str(i)[::-1]:
            print(i)
f = 10
s = 60
print(pal(str,f,s))
22/09/2024
1)arr = [-1, 3, -2, 4, -5, 6]
def ls(arr):
    max_sum = 0
    cs = 0
    for num in arr:
        cs = max(num,cs+num)
        max_sum = max(max_sum , cs)
    return max_sum
print(ls(arr))
2)arr = [1,2,3,4,5,6,7]
k=3
def rt(arr,k):
    
    return arr[-k:] + arr[:-k]
print(rt(arr,k))
3)def a(s1,s2):
    return sorted(s1) == sorted(s2)
s1='eta'
s2='ate'
print(a(s1,s2))
4)def fns(s):
    cf = {}
    for char in s:
        if char in cf:
            cf[char]+=1
        else:
            cf[char]=1
    for char in s:
        if cf[char]==1:
            return char
s = "aabcca"
print(fns(s))
24/09/24
1) longest palindrome
def ls(s):
    n=len(s)
    l = ""
    for i in range(n):
        for j in range(i, n):
            substring = s[i:j+1]
            if substring == substring[::-1] and len(substring) > len(l):
                l = substring
    return l
s = "babcd"
print(ls(s))
 2) def fab(n):
    seq = [0,1]
    for i in range(2,n):
        next_value = seq[i-1] + seq[i-2]
        seq.append(next_value)
    return seq
print(fab(10))
    
    



