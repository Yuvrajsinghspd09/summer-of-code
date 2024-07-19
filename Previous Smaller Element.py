def previous_smaller_element(arr):
    result = [-1] * len(arr)
    stack = []

    for i in range(len(arr)):
        while stack and arr[stack[-1]] > arr[i]:
            stack.pop()
        if stack:
            result[i] = arr[stack[-1]]
        stack.append(i)

    return result

# Example usage
arr = [4, 5, 2, 10, 8]
print(previous_smaller_element(arr))  # Output: [-1, 4, -1, 2, 2]


#brute force
def previous_smaller_element_brute(arr):
    n = len(arr)
    result = [-1] * n
    for i in range(n):
        for j in range(i - 1, -1, -1):
            if arr[j] < arr[i]:
                result[i] = arr[j]
                break
    return result

# Example usage
arr = [4, 5, 2, 10, 8]
print(previous_smaller_element_brute(arr))  # Output: [-1, 4, -1, 2, 2]
