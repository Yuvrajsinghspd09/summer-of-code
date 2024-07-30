def next_smaller_element(arr):
    result = [-1] * len(arr)
    stack = []

    for i in range(len(arr)):
        while stack and arr[stack[-1]] > arr[i]:
            index = stack.pop()
            result[index] = arr[i]
        stack.append(i)

    return result

# Example usage
arr = [4, 5, 2, 10, 8]
print(next_smaller_element(arr))  # Output: [2, 2, -1, 8, -1]

#brute force
def next_smaller_element_brute(arr):
    n = len(arr)
    result = [-1] * n
    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                result[i] = arr[j]
                break
    return result

# Example usage
arr = [4, 5, 2, 10, 8]
print(next_smaller_element_brute(arr))  # Output: [2, 2, -1, 8, -1]



#practice attempt 1
def nse(arr):
    result = [-1]*len(arr)
    stack=[]
    for i in range(len(arr)):
        while stack and arr[stack[-1]]>arr(i):
            index = stack.pop
            result[index]=arr(i)  

        stack.append(i)
    return result
