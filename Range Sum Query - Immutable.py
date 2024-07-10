# optimal approach using prefix sum

'''
The final time complexity depends on how we define it:

If we consider only the query operation (sumRange):

The time complexity is O(1) per query.


If we consider the entire lifecycle of the object, including initialization:

Initialization: O(n)
m queries: O(m)
Total time complexity: O(n + m), where n is the length of the input array and m is the number of queries.



In the context of this problem, we typically focus on the query time complexity, which is O(1). This is because the initialization is done only once, while the sumRange method may be called many times.
'''
class NumArray:
    def __init__(self, nums: List[int]):
        self.prefix_sum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.prefix_sum[i + 1] = self.prefix_sum[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right + 1] - self.prefix_sum[left]

# brute force approach - works fine too
class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right+1])
