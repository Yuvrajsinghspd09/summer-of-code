
'''
Explanation of the else Block:
The else block is associated with the while loop, not the if statement. 
In Python, a while loop can have an else clause which is executed only if the loop completes normally (i.e., it is not terminated by a break statement).
'''

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            while stack and asteroid < 0 < stack[-1]:
                if stack[-1] < -asteroid:
                    stack.pop()
                    continue
                elif stack[-1] == -asteroid:
                    stack.pop()
                break
            else:
                stack.append(asteroid)
        return stack
