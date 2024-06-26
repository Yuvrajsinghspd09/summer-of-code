'''
The time complexity of this solution is O(n), where n is the number of nodes in the binary tree, as each node is visited once in the worst case. The space complexity is O(h), where h is the height of the binary tree, due to the recursive calls on the function call stack.

'''

class Treenode:
    def __init__(self,val=0,right=None,left=None):
        self.val=val
        self.left=left
        self.right=right

def Is_symmetric(root:Treenode)->bool:
    def check_mirror(t1:Treenode,t2:Treenode)->bool:
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return (t1.val==t2.val) and check_mirror(t1.right,t2.left) and check_mirror(t1.left,t2.right)
    
    return check_mirror(root,root)


'''
Here's a visual representation of how check_mirror(root, root) works:

root
             /     \
           left    right
          subtree  subtree

check_mirror(root, root)
  |
  |-- check_mirror(left, right)
        |
        |-- check_mirror(left.left, right.right)
        |-- check_mirror(left.right, right.left)
'''

#practice attempt 1
class treenode(self,val=0,left=Nonw,right=None):
    self.val=val
    self.left=left
    self.right=right

def is_symm(root:treenode)->bool:
    def check_mirror(t1:treenode,t2:treenode)->bool:
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False

        return (t1.val==t2.val) and check_mirror(t1.right,t2.left) and check_mirror(t1.left,t2.right)
    return check_mirror(root,root)
