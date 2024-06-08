'''
Given an inorder traversal array, we can check if it's sorted and there are no duplicate values. 
If both conditions are met, it's possible that the inorder traversal represents a valid BST.
'''

class Solution:
    def isBSTTraversal(self, inorder):
        # Step 1: Check for duplicate values
        seen = set()
        for num in inorder:
            if num in seen:
                return False
            seen.add(num)

        # Step 2: Check if the inorder traversal is sorted
        for i in range(1, len(inorder)):
            if inorder[i] < inorder[i - 1]:
                return False

        # If both conditions are met, it's a valid BST inorder traversal
        return True
'''
Overall, the time complexity is O(n).
The space complexity is O(u), where u is the number of unique elements in the inorder traversal.


'''