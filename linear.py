def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i 
        return -1
arr = [10, 15, 20, 30]
target = 30 
result = linear_search(arr, target)
if result != -1:
    print('Element found at index', result)
else:
    print('Element not found')