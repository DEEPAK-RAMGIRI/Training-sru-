from collections import deque,defaultdict
class TreeNode:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

root = TreeNode(9)
root.left  = TreeNode(5)
root.right = TreeNode(10)
root.left.left = TreeNode(1)
root.left.right = TreeNode(7)
root.left.right.left = TreeNode(6)
root.right.left = TreeNode(8)
root.right.right = TreeNode(12)


# Time Complexcity O(n)
# Space Complexcity O(h) 
def printing(root):
    if root:
        printing(root.left)
        print(root.data,end=" ")
        printing(root.right)
# printing(root)

# Time Complexcity O(n)
# Space Complexcity O(h)
def level_order(root):
    ans = []
    queue = deque([root])
    while queue:
        arr = []
        flag = False
        n = len(queue)
        for _ in range(n):
            current = queue.popleft() 
            arr.append(current.data)
            if current.left:
                queue.append(current.left)
                flag = True
            if current.right:
                queue.append(current.right)
                flag =False
        ans.append(arr)
    return ans

print(level_order(root))
    
    
# printing in zigzag pattern

# Time Complexcity O(n)
# Space Complexcity O(h)
def zigzag(root):
    queue = deque([root])
    ans = []
    flag = False
    while queue:
        arr = []
        n = len(queue)
        flag = not flag
        for _ in range(n):
            current = queue.popleft()
            arr.append(current.data)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        ans.append(arr if flag else arr[::-1])
    return ans
print(zigzag(root))



# left side of tree
# Time Complexcity O(n)
# Space Complexcity O(h)
def left_side(root):
    ans = []
    queue = deque([root])
    while queue:
        arr = []
        n = len(queue)
        for i in range(n):
            current = queue.popleft()
            if i == 0:
                arr.append(current.data)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        ans.append(arr)
    return ans
print(left_side(root))



# Right view
# Time Complexcity O(n)
# Space Complexcity O(h)
def right_view(root):
    ans = []
    queue = deque([root])
    while queue:
        arr = []
        n = len(queue)
        for i in range(n):
            current = queue.popleft()
            if i == n-1:
                arr.append(current.data)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        ans.append(arr)
    return ans
print(right_view(root))






maps = []
def down_view(root):
    if not root: return 
    
# Print the path of the node
node = root.left.right.left
ans = []
def find_path(root,node):
    if not root: return False
    elif node == root:
        ans.append(root.data)
        return True
    if find_path(root.left,node):
        ans.append(root.data)
        return True
    if find_path(root.right,node):
        ans.append(root.data)
        return True
    return False

# Optimsed version 🔥
ans = []
def find_path(root,node,arr):
    if not root: return 
    if root == node:
        
        ans.append(arr +[root.data])
        return
    find_path(root.left,node,arr + [root.data])
    find_path(root.right,node,arr + [root.data])
    return

find_path(root,node,[])
print(ans[::-1])
         
# top view
# using bfs
def down_view_bfs(root,index):
    queue = deque([(root,index)])
    maps = dict()
    while queue:
        Current,index = queue.popleft()
        maps[index] = Current.data
        if Current.left:
            queue.append((Current.left,index - 1))
        if Current.right:
            queue.append((Current.right,index + 1))
    return maps
print(sorted(down_view_bfs(root,0).values()))

maps = dict()
def  down_view_dfs(root,index):
    if not root: 
        return
    maps[index] = root.data
    down_view_dfs(root.left,index - 1)
    down_view_dfs(root.right,index + 1)

down_view_dfs(root,0)
print(sorted(maps.values()))


# TOP VIEW
def top_view_bfs(root,index):
    queue = deque([(root,index)]) 
    maps = dict()
    while queue:
        current,index =  queue.popleft()
        if index not in maps:
            maps[index] = current.data
        if current.left:
            queue.append((current.left,index - 1))
        if current.right:
            queue.append((current.right,index + 1))
    return maps
print(sorted(top_view_bfs(root,0).values()))

maps = dict()
def top_view_dfs(root,index):
    if not root: return
    if index not in maps:
        maps[index] = root.data
    top_view_dfs(root.left,index - 1)
    top_view_dfs(root.right,index + 1)
    return

top_view_dfs(root,0)
print(sorted(maps.values()))
    
         
# find the LCA for BST
def find_lca(root,p,q):
    if not root: return root
    elif root.data > p and root.data > q:
        return find_lca(root.left,p,q)
    elif root.data < p and root.data < q:
        return find_lca(root.right,p,q)
    else: return root.data

print(find_lca(root,1,7))


    
    
    
root = TreeNode(9)
root.left  = TreeNode(10)
root.right = TreeNode(8)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.left.right.left = TreeNode(6)
root.right.left = TreeNode(1)
root.right.right = TreeNode(12)



def lca_in_tree(root,p,q):
    if not root: return None
    elif root.data == p or root.data == q:
        return root.data
    left = lca_in_tree(root.left,p,q)
    right = lca_in_tree(root.right,p,q)
    if left and right: return root.data
    return left if left is not None else right

print(lca_in_tree(root,3,10))


# Nuber of cameras required to moniter nodes
# time complexcity O(n)
#Space complexcity O(h)
visit = [False] * 8
count = [0]
def solve(root):
    if not root: return 1
    left= solve(root.left)
    right = solve(root.right)
    if left == 1 and right == 1:
        return 2
    if left == 2 or right == 2:
        count[0] +=1
        return 3
solve(root)
# print(count[0])

# BCR
# heap implementations