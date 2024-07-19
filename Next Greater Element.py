def next_greater_element(arr):
    result = [-1] * len(arr)  # Initialize the result array with -1
    stack = []  # Initialize an empty stack to keep track of indices

    for i in range(len(arr)):
        # While the stack is not empty and the current element is greater than the element
        # at the index stored at the top of the stack, update the result for that index
        while stack and arr[stack[-1]] < arr[i]:
            index = stack.pop()  # Pop the index from the stack
            result[index] = arr[i]  # Update the result for that index
        # Push the current index onto the stack
        stack.append(i)

    return result

# Example usage
arr = [4, 5, 2, 10, 8]
print(next_greater_element(arr))  # Output: [5, 10, 10, -1, -1]
