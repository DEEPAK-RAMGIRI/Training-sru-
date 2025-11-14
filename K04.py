class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
def insert(root,data):
    if not root:
        return Node(data)
    elif root.data < data:
        root.left = insert(root.left,data)
    elif root.data > data: 
        root.right =  insert(root.right,data)
    return root
    
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)
def preorder(root):
    if root:
        print(root.data,end=" ")
        preorder(root.left)
        preorder(root.right)
   
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data,end= " ")
      
from collections import deque  
def levelorder(root):
    queue = deque([root])
    final = []
    while  queue:
        n = len(queue)
        ans = []
        for i in range(n):  
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            ans.append(node.data)
        final.append(ans)
    print(final)
        
        
                   
root = None
arr = [1,2,3,4,5]
for i in arr:
    root = insert(root,i)
    
levelorder(root)