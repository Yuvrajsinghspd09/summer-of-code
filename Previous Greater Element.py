def previous_greater_element(arr):
    result = [-1] * len(arr)
    stack = []

    for i in range(len(arr)):
        while stack and arr[stack[-1]] < arr[i]:
            stack.pop()
        if stack:
            result[i] = arr[stack[-1]]
        stack.append(i)

    return result

# Example usage
arr = [4, 5, 2, 10, 8]
print(previous_greater_element(arr))  # Output: [-1, -1, 5, -1, 10]
