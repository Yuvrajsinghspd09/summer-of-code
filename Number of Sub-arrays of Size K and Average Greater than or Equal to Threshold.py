# this is the optimal approach with O(n) time complexity
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        threshold_sum = k* threshold
        count = 0
        curr_sum= sum(arr[:k])
        if curr_sum>=threshold_sum:
            count+=1
        for i in range(k,n):
            curr_sum += arr[i] - arr[i - k]
            if curr_sum>=threshold_sum:
                count+=1
        return count


# brute force with o(n*k) - time limit exceeded
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        threshold_sum = k * threshold  # Calculate the total threshold sum
        count = 0
        
        for i in range(n - k + 1):
            curr_sum = sum(arr[i:i + k])  # Calculate sum of the subarray starting at index i
            if curr_sum >= threshold_sum:  # Check if the average is greater than or equal to the threshold
                count += 1
                
        return count

# Example usage
arr = [2, 1, 3, 4, 1, 1, 3, 4]
k = 3
threshold = 3
solution = Solution()
print(solution.numOfSubarrays(arr, k, threshold))  # Output should be the number of subarrays meeting the condition
