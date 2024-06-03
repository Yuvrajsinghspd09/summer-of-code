# Notes for basic 2pointer implementation
#Problem 1--> to find numbers which sum up to zero

'''
def two_pointer_method(arr):  # arr is sorted here
    left=0
    right=len(arr)-1

    while left<right:
        if arr[left]+arr[right]==0:
            left += 1             # left+=1 is here to find all possible pairs
            right -= 1         #right-=1 is here to find all possible pairs, 
            #otherwise would give only the pair which it encounters first
            return arr[left],arr[right]
        elif arr[left]+arr[right]<0:
            left+=1
        else:
            right-=1


array=[-2,-1,0,1,2]
print(two_pointer_method(array))

'''
#Problem 2--> Finding a Pair in a Sorted Array with a Given Sum
'''
def find_a_pair(arr1,sum):
    left=0
    right=len(arr1)-1
    while left<right:
        if arr1[left]+arr1[right]==sum:
            left += 1
            right -= 1
            ## left+=1 is here to find all possible pairs
            #right-=1 is here to find all possible pairs, 
            #otherwise would give only the pair which it encounters first
            return arr1[left],arr1[right]
        elif arr1[left]+arr1[right]<sum:
            left+=1
        else:
            right-=1
    return None  # if no pair is found

arraynums = [1,2,3,4,5,6,7,8]
sum=9
print(find_a_pair(arraynums,sum))


'''

#3--> Reversing an Array
'''
def reverse_array(nums):
    if len(nums)==1:
        print("no need to reverse")
    elif len(nums)==0:
        print("empty array")
    else:
        left=0
        right=len(nums)-1
        while left<=right:
            nums[left], nums[right] = nums[right], nums[left]
            left+=1
            right-=1
        return nums

nums=[1,2,3,4,5]
nums1=[1,2,3,4,5,6]
print(reverse_array(nums))
print(reverse_array(nums1))

'''


#4--> check for palindrome

def check_palindrome(string):
    if len(string)==1:
        print("no need to check")
    elif len(string)==0:
        print("empty string")
    else:
        left=0
        right=len(string)-1
        while left < right:
            if string[left] != string[right]:
                return False
            left += 1
            right -= 1
        return True
    

print(check_palindrome("racecar"))  
print(check_palindrome("hello"))