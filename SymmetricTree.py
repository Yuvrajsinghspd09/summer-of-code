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
