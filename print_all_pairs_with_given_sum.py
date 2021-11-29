def pairedelements(arr, targetSum):
    arr.sort()
    low = 0
    high = len(arr) - 1
    while low < high:
        if arr[low] + arr[high] == targetSum:
            print((arr[low], arr[high]))
        if arr[low] + arr[high] > targetSum:
            high -= 1
        else:
            low += 1


arr = [2, 3, 4, -2, 6, 8, 9, 11]
pairedelements(arr, 6)
