'''
Conditions for Checking a Rotated Sorted Array
Count Break Points: Traverse the array and count the number of times the current element is greater than the next element.
Valid Array:
If the array is still sorted, there will be 0 break points.
If the array is a rotated version of a sorted array, there will be exactly 1 break point.
Any other number of break points indicates the array is neither sorted nor a rotated sorted array.
 expression (i + 1) % n helps wrap around the array:
'''

def check(nums):
    count_breaks = 0
    n = len(nums)
    
    for i in range(n):
        if nums[i] > nums[(i + 1) % n]:
            count_breaks += 1
    
    return count_breaks <= 1
