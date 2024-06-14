def rotateString(s: str, goal: str) -> bool:
    # Step 1: Check if lengths are different
    if len(s) != len(goal):
        return False
    
    # Step 2: Concatenate s with itself
    combined = s + s
    
    # Step 3: Check if goal is a substring of the concatenated string
    return goal in combined
'''
Time Complexity:
Checking the length of two strings: O(1).
Concatenation of the string s with itself: 
O(n), where n is the length of s.
Checking if goal is a substring of the concatenated string: 
O(n) on average due to efficient substring search algorithms.
Thus, the overall time complexity is O(n).

Space Complexity:
Creating the concatenated string s+s requires 
O(n) additional space.
Therefore, the space complexity is O(n).

'''
# practice attempt 1
def rotate_string(s,goal):
    if len(s)!=len(goal):
        return False
    combined = s+s
    return goal in combined:
        
    
