
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        balance = 0
        
        for char in s:
            if char == '(':
                stack.append(char)
            else:
                if stack:
                    stack.pop()
                else:
                    balance += 1
        
        return balance + len(stack)



'''
example string = "())"

We start with an empty stack and balance set to 0.
We iterate through the string "()":

For the first character (, we append it to the stack, so stack = ['('].
For the second character ), we pop the top element from the stack, so stack becomes empty.
For the third character ), since the stack is empty, we increment balance by 1, so balance = 1.


After iterating through the entire string, balance = 1 and len(stack) = 0.
We return balance + len(stack), which is 1 + 0 = 1
'''