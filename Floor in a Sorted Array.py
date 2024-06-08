def find_floor_index(arr, x):
    left, right = 0, len(arr) - 1
    floor_index = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            floor_index = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return floor_index

# Example usage
arr1 = [1, 2, 8, 10, 12, 14, 19]
x1 = 5
print(find_floor_index(arr1, x1))  # Output: 1 (the floor is 2)

