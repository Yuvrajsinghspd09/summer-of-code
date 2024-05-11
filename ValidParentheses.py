'''
EXPLANATION
If the character is a closing bracket:
  Check if the stack is not empty; if empty, assign '#' to top_element.
  Compare top_element (the top of the stack) with the corresponding opening bracket using the mapping.
       If they don't match, return False (invalid string).

If the character is an opening bracket:
Push it onto the stack.

After iterating through the entire string:
  Check if the stack is empty.
  If empty, return True (valid string).
  If not empty, return False (invalid string).

'''

def isValid(s):
    stack = []

    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:
            #HERE WE CHECK FOR CLOSING BRACKET
            # Check if the stack is not empty; if empty, assign '#' to top_element
            if stack:
                top_element = stack.pop()
            else:
                top_element = '#'

             # Compare the top of the stack with the corresponding opening bracket
            if mapping[char] != top_element:
                # If they don't match, the string is invalid
                return False
            
        else:
            # If the character is an opening bracket, push it onto the stack
            stack.append(char)
     # If empty, all brackets are valid and matched
    return not stack