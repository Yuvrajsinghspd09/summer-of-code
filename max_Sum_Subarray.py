def max_sum_subarray(arr, K):
    n = len(arr)
    if n < K:
        return -1

    # Calculate the sum of the first window of size K
    max_sum = sum(arr[:K])
    window_sum = max_sum

    # Slide the window from start to end of the array
    for i in range(n - K):
        # Subtract the element going out of the window and add the element coming into the window
        window_sum = window_sum - arr[i] + arr[i + K]
        max_sum = max(max_sum, window_sum)

    return max_sum

        

# Example usage
nums = [1, 3, 2, 10, 6, 3, 3]# (k=1,left=0, sum=1)(k=2,left=0,sum=4)(k=3,left=0,sum=6)()
k = 3
result = max_sum_subarray(nums, k)
print(f"Maximum sum subarray of size {k} is: {result}")