def binary_search(arr, target):
    if len(arr) == 0:
        return 0
    
    left = -1
    right = len(arr)

    while (right - left) > 1:
        middle = (right + left) // 2
        if arr[middle] < target:
            left = middle
        elif arr[middle] > target:
            right = middle
        else:
            return middle
    
    return None

binary_search([1, 2, 3, 4, 6, 7, 8, 9, 12, 34, 244, 345], 8)