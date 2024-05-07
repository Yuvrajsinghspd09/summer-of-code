#ANOTHER APPROACH BELOW THIS SOLUTION
def majority_element(nums):
    counts ={}

    for num in nums:
        if num in counts:
            counts[num]+=1
        else:
            counts[num]=1

    n = len(nums)
    for num,count in counts.items():
        if count > n/2 :
            return num
        
    # Step 4: If no majority element found, return None or any default value
    return None

nums = [1, 2, 2, 2, 5, 2, 4, 2]

# Find the majority element
result = majority_element(nums)
print("Majority element:", result)

'''
Time Complexity Analysis:
Constructing the hash map: O(n), where n is the length of the array.
Checking the counts in the hash map: O(m), where m is the number of unique elements in the array.
Overall, the time complexity is O(n + m) for this approach.

Space Complexity Analysis:
Hash map space: O(m), where m is the number of unique elements in the array.
The space complexity is O(m) for this approach due to the hash map used to store element counts.
'''




def majority_element(nums):
    # Step 1: Sort the array
    nums.sort()

    # Step 2: Find the middle element(s)
    n = len(nums)
    mid = n // 2
    middle_elements = []
    if n % 2 == 1:
        middle_elements.append(nums[mid])
    else:
        middle_elements.extend([nums[mid], nums[mid - 1]])

    # Step 3: Check for majority element(s)
    for num in middle_elements:
        if nums.count(num) > n // 2:
            return num

    # If no majority element found, return None or any default value
    return None

nums = [1, 2, 2, 2, 5, 2, 4, 2]
result = majority_element(nums)
print("Majority element:", result)

'''
Time Complexity: O(n log n) due to sorting the array. The counting of occurrences in the middle elements takes linear time.
Space Complexity: O(1) because we don't use any extra space proportional to the input size.
'''