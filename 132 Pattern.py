#optimal 
def find132pattern(nums):
    stack = []
    third = float('-inf')
    
    for num in reversed(nums):
        if num < third:
            return True
        while stack and num > stack[-1]:
            third = stack.pop()
        stack.append(num)
    
    return False



# better but TLE error
def find132pattern(nums):
    n = len(nums)
    for j in range(1, n-1):
        min_i = min(nums[:j])
        for k in range(j+1, n):
            if min_i < nums[k] < nums[j]:
                return True
    return False

# brute force
def find132pattern(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if nums[i] < nums[k] < nums[j]:
                    return True
    return False
