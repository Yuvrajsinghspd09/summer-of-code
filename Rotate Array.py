#Reverse Method (O(n) time, O(1) space):
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse_elements(start,end):
            while start<end:
                nums[start],nums[end]= nums[end],nums[start]
                start+=1
                end-=1
            
        n=len(nums)
        k=k%n
        reverse_elements(0,n-1)
        reverse_elements(0,k-1)
        reverse_elements(k,n-1)




#Using Extra Array (O(n) time, O(n) space)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n  # Handle cases where k > n
        rotated = [0] * n
        
        for i in range(n):
            rotated[(i + k) % n] = nums[i]
        
        nums[:] = rotated
