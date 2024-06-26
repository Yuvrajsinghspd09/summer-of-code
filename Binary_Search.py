#method 1#
#The time complexity of binary search is O(logn)
'''
The space complexity depends on the implementation:

Iterative implementation: The space complexity is O(1) because it only uses a constant amount of extra space for variables (left, right, and mid).
Recursive implementation: The space complexity is 
O(logn) due to the recursion stack. Each recursive call adds a layer to the stack, and there are at most logn recursive calls in a balanced search.
'''
def binary_search_iterative(arr,target):
    if arr =="":
        return "empty array"
    else:
        left=0
        right=len(arr)-1
        while left<=right:
            mid= (left+right)//2

            if arr[mid]==target:
                return mid
            elif arr[mid]>target:
                right=mid-1
            else:
                left=mid+1
    
    return -1


# Method 2

def bin_recursive_search(arr,target,left,right):
    if left>right:
        return -1
    
    mid = (left+right)//2

    if arr[mid]==target:
        return mid
    elif arr[mid]>target:
        return bin_recursive_search(arr,target,left,mid-1)
    else:
        return bin_recursive_search(arr,target,mid+1,right)
    


def binary_search(arr, target):
    # Start the recursive search from index 0 to len(arr) - 1
    return bin_recursive_search(arr, target, 0, len(arr) - 1)

# Example usage
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 6

    result = binary_search(arr, target)
    if result != -1:
        print(f"Element {target} found at index {result}")
    else:
        print(f"Element {target} not found in the array")




def binary_search_practice1(array,target):
    if array=="":
        return "empty array"
    left=0
    right=len(array)-1

    while left<=right:
        mid = (left+right)//2
        if target == array[mid]:
            return mid
        elif target>array[mid]:
            left=mid+1
        else:
            right= mid-1

return -1


def binary_search_practice2(array,target):
    if array=="":
        return "empty array"
    left = 0
    right=len(array)-1
    while left<=right:
        mid=(left+right)//2:

        if array[mid]==target:
            return mid
        elif array[mid]>target:
            right=mid-1
        else:
            left=mid+1

   return -1


def binary_search_practice_recursive1(array,target,left,right):
    if left>right:
        return -1

    mid = (left+right)//2
    if array[mid]==target:
        return mid
    elif array[mid]>target:
        return binary_search_practice_recursive1(array,target,left,mid-1)
    else:
        return binary_search_practice_recursive1(array,target,mid+1,right)

def binary_search(array,target):
    return binary_search_practice_recursive1(array,target,0,len(array)-1)
        


#practice attempt3
def binary_search_practice3(arr,target):
    if arr =="":
        return "empty array"
    left=0
    right=len(arr)-1
    while left<=right:
        mid = (left+right)//2
        if target==arr[mid]:
            return mid
        elif target>arr[mid]:
            left = mid+1
        else:
            right=mid-1
    return -1
