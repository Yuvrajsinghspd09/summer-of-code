class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char == '*':
                if stack:  # Check if stack is not empty
                    stack.pop()
            else:
                stack.append(char)
        
        return ''.join(stack)
