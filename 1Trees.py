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


maxi = [0] 
def diameter(root):
    if not root: return 0
    left = diameter(root.left)
    right = diameter(root.right)
    maxi[0] = max(maxi[0],left + right)
    return 1 + max(left ,right) 
    

def isSameTree(p,q):
    # checking if p and q both are not not present either we reached the end   or empty nodes which is true in this case
    if not p and not q: return True
    # if one have node and other dont or the values are not same we return False because they are not same
    if not p or not q or q.val != p.val: return False 
    
    return isSameTree(p.left,q.left) and isSameTree(p.right,q.right)
    
def InvertBinaryTree(root):
    if not root: return 
    root.left,root.right = root.right,root.left
    InvertBinaryTree(root.left) 
    InvertBinaryTree(root.right)   
    
from collections import deque
def Symmetric(root):
    queue = deque([(root.left,root.right)])
    while queue:
        lefty,righty = queue.popleft()
        if not lefty and not righty: continue
        if not lefty or not righty or lefty.val != righty.val: return False 
        
        queue.append((lefty.left,righty.right))
        queue.append((lefty.right,righty.left))
    return True

def ReverseOddLevelbfs(root):
    queue = deque([root])
    level = 1
    while queue:
        n = len(queue)
        for _ in range(n):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)             

        if level & 1:
            i = 0
            j = len(queue) - 1

            while i < j:
                queue[i].val,queue[j].val = queue[j].val, queue[i].val
                i+=1
                j-=1
        level += 1

    return root

def ReverseOddLeveldfs():
    def dfs(left,right,level):
            if not left: return
            if level & 1:
                left.val,right.val = right.val,left.val
            dfs(left.left,right.right,level + 1)
            dfs(left.right,right.left,level + 1)
    dfs(root.left,root.right,1)
    return root

# Binary Tree from Preorder and Inorder Traversal
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
def buildTree(self,preorder, inorder):
    self.index = 0 # index start from 0 beacuse preorder [ROOT LEFT RIGHT]
    def build_tree(start,end):
        if start > end: return None
        i = start
        for i in range(start,end + 1):
            if inorder[i] == preorder[self.index]:
                break
        root = Node(preorder[self.index])
        self.index+=1
        root.left = build_tree(start, i - 1)  # left
        root.right = build_tree(i + 1,end)    # right in the preorder
        return root       
    print(build_tree(0,len(preorder)-1))


# Construct Binary Tree from Inorder and Postorder Traversal

def buildTree(self, inorder, postorder):
    self.index = len(inorder) - 1  # index start from end bcoz of the postorder [LEFT RIGHT ROOT]
    def find(left,right):
        if left > right:
            return None
              
        for i in range(left,right + 1): # loop start from start and end with end + 1
            if postorder[self.index] == inorder[i]:
                break
            
        root = Node(postorder[self.index])
        self.index-=1 # index gonna decrement
        root.right = find(i + 1, right) # right comes first
        root.left = find(left,i  - 1) # left comes next
        return root
    return find(0,len(inorder) -1 )
    
def morris_traversal(root):  
    temp = root
    ans = []
    while temp:
        if not temp.left:
            ans.append(temp.val) # adding temp vales
            temp = temp.right
        else:
            curr =temp.left
            while curr.right and curr.right != temp:
                curr = curr.right
            
            if not curr.right : 
                curr.right = temp
                temp = temp.left
            else:
                ans.append(temp.val) # adding temp vales
                curr.right = None
                temp = temp.right
    print(ans)
               
def hasPathSum(self, root, targetSum):
    if not root: return False 
    if not root.left and not root.right:
            return targetSum == root.val
    return self.hasPathSum(root.left,targetSum - root.val) or self.hasPathSum(root.right,targetSum - root.val) 
           

def sumNumbers(self, root):
    self.sums = 0
    def find(root,curr):
        if not root: return
        if not root.left and not root.right: 
            self.sums += curr*10 + root.val
            return
        find(root.left,curr*10 + root.val)
        find(root.right,curr*10 + root.val)
    find(root,0)
    return self.sums
                
        
                
              
arr = [5,1,2,6,7,3,4]
root = None
for i in arr:
    root = insert(root,i)

print(height(root))
traversal(root,"root")
