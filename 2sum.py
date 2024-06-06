def two_Sum(nums,target):
    dict1={}
    for i,num in enumerate (nums):
     
#we iterate over the nums list using the enumerate function. 
#The enumerate function returns a tuple of the index and the corresponding element from the list.
#So, i represents the index, and num represents the value at that index.
    
        other_num=target-num
        

        if other_num in dict1:
            return [dict1[other_num], i]
'''
 We return a list containing the indices of these two numbers: 
 the value corresponding to other_num (which is the index of the first number), 
 and the current index i (which is the index of the second number).
'''
