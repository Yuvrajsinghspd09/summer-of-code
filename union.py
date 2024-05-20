#Another method below this one

class Solution:
    def findUnion(self, arr1, arr2, n, m):
        union_set = set()
        
        for i in arr1:
            union_set.add(i)
        
        for j in arr2:
            union_set.add(j)
        
        # Convert the set to a sorted list
        arr3 = sorted(union_set)
        
        return arr3
    

    '''
    class Solution:
    
    def findUnion(self, arr1, arr2, n, m):
        # Create an empty list to store the union
        arr3 = []
        
        # Add all elements from arr1 to arr3
        for i in arr1:
            if i not in arr3:
                arr3.append(i)
        
        # Add elements from arr2 to arr3 if they are not already present
        for j in arr2:
            if j not in arr3:
                arr3.append(j)
            sort the list here
        return arr3
    '''

