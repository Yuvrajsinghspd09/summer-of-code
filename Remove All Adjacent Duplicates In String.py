def remove_duplicates_stack(s: str) -> str:
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return ''.join(stack)

# Example usage
s = "abbaca"
print(remove_duplicates_stack(s))  # Output: "ca"
