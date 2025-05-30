#Trees
class Node:
    
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
def insert(root,data):
    if not root:
        return Node(data)
    elif root.data < data :
        root.right = insert(root.right,data)
    else:
        root.left = insert(root.left,data)
    return root

def traversal(value,root):
    if root:
        traversal('left',root.left)
        print(value, root.data,end=" ")
        traversal('right',root.right)
        
#level order traversal       
def levelorder(root):
    q = [root]
    final = []
    while q:
        n = len(q)
        ans = []
        for _ in range(n):
            value = q.pop(0)
            ans.append(value.data)
            if value.left:
                q.append(value.left)
            if value.right:
                q.append(value.right)
        final.append(ans)
    print(final)
        
        
# Count the no of leaf nodes in tree 🌳
def count_leaf_node(root):
    if not root:
        return 0
    elif not root.left and not root.right:
        return 1
    return count_leaf_node(root.left) + count_leaf_node(root.right)


#path to reach leaf node
ans = []
def path_to_reach_the_leaf_node(root,arr):
    if not root:
        return
    elif not root.left and not root.right:
        ans.append(arr+[root.data])
    path_to_reach_the_leaf_node(root.left,arr + [root.data]) 
    path_to_reach_the_leaf_node(root.right,arr+[root.data])
    
    
# Diameter of Binary Tree
def diameter_of_binary_tree(self, root):
        diameter = [0]  # we are using list bcoz int is immutable in function calling and it may effect our answer 
        def findheight(root):
            if not root:
                return 0
            left = findheight(root.left)
            right = findheight(root.right)
            diameter[0] = max(left+right,diameter[0])
            return 1 + max(left,right)
        findheight(root)
        print(diameter[0])
        
        
# code for saving all vertical level order 
def vertical_level_order(root):
    final = dict()
    queue = [(root,0)]
    while queue:
        n = len(queue)
        for _ in range(n):
            value,col = queue.pop(0)
            if col in final:
                final[col].append(value.data)
            else:
                final[col] = [value.data]
                
            if value.left:
                queue.append((value.left,col-1))
            if value.right:
                queue.append((value.right,col+1))
    print(final)

# method 01 for top view       
def top_view(root):
    queue = [(root,0)]
    final = dict()
    while queue:
        n = len(queue)
        ans = []
        for _ in range(n):
            value,col = queue.pop(0)
            if col not in final:
                final[col] = value.data
            if value.left:
                queue.append((value.left,col-1))
            if value.right:
                queue.append((value.right,col+1))
    # if u got this go find top-left and top-right 
    return final
    
# method 02 using top view
def top_view_recursion(root):
    top = dict()
    def top_side(root,col):
        if not root: return
        if col not in top: top[col] = root.data
        top_side(root.left,col+1)
        top_side(root.right,col-1)
    top_side(root,0)
    return top

            
#vertical leval order left view using iteration
#method 01
def left_view(root):
    queue = [root]
    result = []
    while queue:
        n = len(queue)
        for i in range(n):
            node = queue.pop(0)
            if i == 0:
                result.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return result

#method 02 left_view using recursion
def left_view_recursion(root):
    left = dict()
    def left_side(root,col):
        if not root: return 
        if col not in left:
            left[col] = root.data
        left_side(root.left,col+1)
        left_side(root.right,col+1)
    left_side(root,0)
    return left

   #method 1 right view 
def right_view(root):
    queue = [root]
    result = []
    while queue:
        n = len(queue)
        for i in range(n):
            value = queue.pop(0)
            if i == (n-1):
                result.append(value.data)
            if value.left:
                queue.append(value.left)
            if value.right:
                queue.append(value.right)     
    return result
#method 2 right view using recursion
def right_view_recursion(root):
    right = dict()
    def right_side(root,col):
        if not root: return 0
        right[col] = root.data
        right_side(root.left,col+1)
        right_side(root.right,col+1)
    right_side(root,0)
    return right

#method 01 fro bottom -view
def bottom_view(root):
    queue = [(root,0)]
    final = dict()
    while queue:
        n = len(queue)
        ans = []
        for _ in range(n):
            value,col = queue.pop(0)
            final[col] = value.data
            if value.left:
                queue.append((value.left,col-1))
            if value.right:
                queue.append((value.right,col+1))
    # if u got this go find top-left and top-right 
    return final

#method 02
def bottom_view_recursion(root):
    bottom = dict()
    def bottom_side(root,col):
        if not root: return
        bottom[col] = root.data
        bottom_side(root.left,col-1)
        bottom_side(root.right,col+1)
    bottom_side(root,0)
    return bottom

#LOWEST COMMON ANCESTORS FOR BINAEY SEARCH TREE
def lowest_common_ancestors(root,value1,value2):
    if not root:
        return "Broh create tree 🤣"
    if value1 <= root.data <= value2:
        return root.data
    elif value1 >= root.data:
        return lowest_common_ancestors(root.right,value1,value2)
    else:
        return lowest_common_ancestors(root.left,value1,value2)
    
#LOWEST COMMON ANCESTORS FOR BINAEY TREE
def lowest_common_ancestors_for_binary_tree(root,value1,value2):
    if not root: return
    if root.data == value1 or root.data == value2:
        return root
    left = lowest_common_ancestors_for_binary_tree(root.left,value1,value2)
    right = lowest_common_ancestors_for_binary_tree(root.right,value1,value2)
    if left and right: return root
    return None


def sum_of_the_nodes(root,sums):
    if not root:
        return 0 
    return root.data + sum_of_the_nodes(root.left) + sum_of_the_nodes(root.right)

# Some thing is wrong in this not all test cases are passing don't know why. in binary 124    
# def max_path_sum_tree(root,maxi):
#     left = [0]
#     right = [0]
#     def function(root,maxi):
#         if not root:
#             return 0
#         left[0] = max(left[0],root.data + max_path_sum_tree(root.left,maxi))
#         right[0] = max(right[0],root.data + max_path_sum_tree(root.right,maxi))
#         maxi = max(maxi,left+right)
#         return maxi
#     return  function(root,maxi)
def height_of_tree(root):
    if not root: return 0
    return 1 + max(height_of_tree(root.left),height_of_tree(root.right))
def balanced_or_not(root):
    if not root: return 0
    return (height_of_tree(root.left) - height_of_tree(root.right))

root = None
# arr = [3,9,20,15,7,2,1,0]
arr = [20,10,9,15,13,16,12,11,25,21,32,33,34,35,36]
# arr = [4,2,1,3,6,5,7]
for i in arr:
    root = insert(root,i)
# print(count_leaf_node(root))
# path_to_reach_the_leaf_node(root,[])
# print(ans)

# levelorder(root)
# vertical_level_order(root)

# print(left_view(root))
# print(left_view_recursion(root))

# print(right_view(root))
# print(right_view_recursion(root))

# print(max_path_sum_tree(root))
# print(diameter_of_binary_tree(root))

# for i in top_view(root).values(): print(i,end=" ")
# print()
# for i in top_view_recursion(root).values(): print(i,end=" ")
# print()
# for i in bottom_view_recursion(root).values(): print(i,end=" ")
# print()
# for i in bottom_view(root).values(): print(i,end=" ")
# print()

# print(lowest_common_ancestors(root,25, 37))

# traversal('root',root)

# print(max_path_sum_tree(root,0))
print(balanced_or_not(root))
if balanced_or_not(root) <= 0:
    print("Balanced Tree")
else:
    print("Not balanced tree")
    
        