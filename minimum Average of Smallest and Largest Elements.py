class Solution:
    def minimumAverage(self, nums: list[int]) -> float:
        nums.sort()  # Sort the array to access smallest and largest elements easily
        averages = []
        l, r = 0, len(nums) - 1  # Two pointers at the start and end of the array

        while l < r:
            # Calculate the average of the smallest and largest
            avg = (nums[l] + nums[r]) / 2
            averages.append(avg)

            # Move pointers inward
            l += 1
            r -= 1

        # Return the minimum of all computed averages
        return min(averages)
