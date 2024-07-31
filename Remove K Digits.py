'''
Step-by-Step Explanation:
Initial Stack Processing:

As we iterate through the digits of the number, we keep removing larger preceding digits when a smaller digit is encountered.
This process ensures that the digits in the stack are in an order that gives us the smallest possible number up to that point.
Post-Iteration Removal:

After the iteration, if k is still greater than 0, it means we haven't removed enough digits.
Removing from the end ensures that we are trimming the number further without disrupting the already optimized smaller digits at the beginning of the stack.
'''

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        for digit in num:
            # While we can remove digits and the current digit is smaller than the last in the stack
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()  # Remove the last digit to maintain the smallest number
                k -= 1
            stack.append(digit)  # Add the current digit to the stack
        
        # If there are still remaining digits to remove, remove from the end
        while k > 0:
            stack.pop()
            k -= 1
        
        # Convert to string and remove leading zeros
        result = ''.join(stack).lstrip('0')
        
        # Return '0' if result is empty
        return result if result else "0"




#practice attempt 1

class Solution:
  def removeKdigit(self, num:str, k:int) -> str:
    stack=[]
    for digit in num:
      while stack and k>0 and stack[-1]>digit:
        stack.pop()
        k-=1
      stack.append(digit)

    while k>0:
      stack.pop()
      k=-1
    
    result= ''.join(stack).lstrip('0')
    return result if result else 0
