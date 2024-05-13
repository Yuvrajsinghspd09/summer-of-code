def max_product_subarray(nums):
    if not nums:
        return 0

    n = len(nums)
    max_product = min_product = result = nums[0]

    for i in range(1, n):
        if nums[i] < 0:
            max_product, min_product = min_product, max_product

        max_product = max(nums[i], max_product * nums[i])
        min_product = min(nums[i], min_product * nums[i])

        result = max(result, max_product)

    return result