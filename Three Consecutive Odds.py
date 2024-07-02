# solution 1
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0
        for num in arr:
            if num % 2 == 1:
                count += 1
                if count == 3:
                    return True
            else:
                count = 0
        return False
    
# solution 2
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        def is_odd(num):
            return num % 2 == 1

        for i in range(len(arr) - 2):
            if is_odd(arr[i]) and is_odd(arr[i+1]) and is_odd(arr[i+2]):
                return True
        
        return False

# solution 3
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(len(arr) - 2):
            if arr[i] % 2 == 1 and arr[i+1] % 2 == 1 and arr[i+2] % 2 == 1:
                return True
        return False