'''
Do we need to specify left += 1 and right -= 1?
No, we don't need to do this explicitly. Here's why:

When nums[mid] < nums[mid + 1], we set left = mid + 1. This effectively increases left by at least 1.
When nums[mid] >= nums[mid + 1], we set right = mid. This effectively decreases the right bound, though not necessarily by 1.


Why do we return left at the end?
When the while loop ends, left and right will have converged to the same value, which is a peak element. We return left (we could also return right as they're equal at this point) because it represents the index of a peak element.
How does left have the value of the peak element?
The algorithm ensures that left converges to a peak. Here's how:

If nums[mid] < nums[mid + 1], we move left to mid + 1. This means we're always moving towards higher values.
If nums[mid] >= nums[mid + 1], we keep mid in our search range by setting right = mid.
The loop continues until left and right meet. When they do, we've found a peak.



Let's walk through an example to illustrate:
Consider the array: [1, 2, 3, 1]

Initial state: left = 0, right = 3
mid = (0 + 3) // 2 = 1
nums[1] < nums[2], so left = mid + 1 = 2
Next iteration: left = 2, right = 3
mid = (2 + 3) // 2 = 2
nums[2] > nums[3], so right = mid = 2
The loop ends because left == right == 2

At this point, we've found a peak at index 2 (value 3). We return left, which is 2.

'''
# O(log(n))- time complexity
def find_peak_elem(nums):
    left=0
    right=len(nums)-1
    mid= (left+right)//2
    
    while left<right:
        if nums[mid]<nums[mid+1]:
            left=mid+1
        else:
            right=mid
    return left
