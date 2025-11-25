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
    
# Time Complexcity O(n)
# Space complexcity O(n) (stack space)

# DFS methods
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
      
      
# Time Complexcity O(n)
# Space Complexcity O(n)
# BFS Method 
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
    
# levelorder(root)
# Threaded Binary Tree
# Threaded Binary Tree TBT
# A threaded binary tree is same as BT but the leaf nodes left and right pointer which is none
# in a BT will be storing predesessor and successor in TBT
# There are 2 types of threaded binary tree 
# ----------------> Single threaded binary tree
# ----------------> Double Threaded Binary tree
# left pointer stores pedesser and right side store successor


# Morris traversal
# Time Complexcity O(n)
# Space complexcity O(n)
# Single Threaded Tree
def morris(root):
    temp = root
    while temp:
        if temp.left:
            curr = temp.left
            while curr.right and curr.right != temp:
                curr = curr.right
            if curr.right:
                curr.right = None
                print(temp.data)
                temp = temp.right
            else:
                curr.right = temp
                temp = temp.left
        else:
            print(temp.data)
            temp = temp.right

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.lt  = True
        self.rt = True
        
def insert(root,data):
    curr = root
    while curr:
        parent = curr
        if data < curr.data:
            if not curr.lt: 
                curr = curr.left
            else:
                break
        else:
            if not curr.rt:
                curr = curr.right
            else:
                break
    node = Node(data)
    if  data < parent.data:
        node.left = parent.left
        node.right = parent
        parent.left = node
        parent.lt = False    
    else:
        node.left = parent
        node.right = parent.right
        parent.right = node
        node.rt = False
    return node
                
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
def insert(root,data):
    if not root:
        return Node(data)
    elif root.data > data:
        root.left = insert(root.left,data)
    elif root.data < data: 
        root.right =  insert(root.right,data)
    return root
    

# DFS  Views
# Time Complexcity O(n)
# Space ComplexcityO(h)
ans = dict()
def topview(root,index):
    if not root: return
    if index not in ans:
        ans[index] = root.data
    topview(root.left,index - 1)
    topview(root.right,index + 1)

ans = dict()
def  bottomview(root,index):
    if not root: return
    ans[index] = root.data
    bottomview(root.left,index - 1)
    bottomview(root.right,index + 1)
  
ans = dict()  
def leftview(root,index):
    if not root: return
    if index not in ans:
        ans[index] = root.data
    leftview(root.left,index + 1)
    leftview(root.right,index + 1)
    
ans = dict()  
def rightview(root,index):
    if not root: return
    ans[index] = root.data
    rightview(root.left,index + 1)
    rightview(root.right,index + 1)
    
    
# BFS
from collections import defaultdict,deque
def levelorder_views(root):
    ans = defaultdict(list)
    queue = deque([(root,0)])
    while queue:
        node,level = queue.popleft()
        ans[level].append(node.data)
        if node.left:
            queue.append((node.left,level + 1))
        if node.right:
            queue.append((node.right,level + 1))
    
    leftview = []
    rightview = []
    for i,j in ans.items():
        leftview.append(j[0])
        rightview.append(j[-1])
        # print(j)
    print(leftview)
    print(rightview)
    

        
        
     

arr = [7,5,9,1,8,6,10]
root = None
for i in arr:
    root = insert(root,i)
    
    
# topview(root,0)
# print(ans.values())

# bottomview(root,0)
# print(ans.values())

# leftview(root,0)
# print(ans.values())

# rightview(root,0)
# print(ans.values())
    
levelorder_views(root)