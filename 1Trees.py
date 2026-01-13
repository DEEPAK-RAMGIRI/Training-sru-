class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def insert(root,val):
    if not root:
        return Node(val)
    if root.data > val:
        root.left = insert(root.left,val)
    else:
        root.right = insert(root.right,val)
    return root

def traversal(root,node):
    if root:
        traversal(root.left,"left")
        print(node,root.data,end=" ")
        traversal(root.right,"right")
        
        
def height(root):
    if not root: return 0
    return 1 + max(height(root.left) ,height(root.right))
        
arr = [5,1,2,6,7,3,4]
root = None
for i in arr:
    root = insert(root,i)

print(height(root))
traversal(root,"root")
