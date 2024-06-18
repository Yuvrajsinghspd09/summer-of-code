class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num ==0 :
            return True
        elif num%10 ==0 :
            return False
        else :
            return True
        
'''
code is already efficient and correct.
 However, we can simplify it slightly for better readability. 
 Specifically, we can remove the elif and else statements
 since the return statements already exit the function:
'''
class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num == 0:
            return True
        if num % 10 == 0:
            return False
        return True


#practice attempt 1
def double_rev(num):
    if num==0:
        return True
    if num%10==0:
        return False
    return True
