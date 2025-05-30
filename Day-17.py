#Trees
class Tree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
def insert(root,data):
    if not root:
        return Tree(data)
    elif root.data < data:
        root.right = insert(root.right,data)
    else:
        root.left = insert(root.left,data)
    return root

def traversal(value,root):
    if root:
        traversal('left',root.left)
        print(value,root.data,end=" ")
        traversal('right',root.right)
        
        
def total_path_sum(root):
    if not root:
        return 0
    return root.data + total_path_sum(root.left) + total_path_sum(root.right)

def longest_diameter(root):
    diameter = [0]
    def find_height(root):
        if not root:return 0
        left = find_height(root.left)
        right = find_height(root.right)
        diameter[0] = max(diameter[0],left+right)
        return 1 + max(left,right)
    find_height(root)
    return diameter[0]

def max_sum_path(root):
    if not root: return 0
    max_sum = [root.data]

    def find_max_sum(root):
        if not root: return 0
        left = max(0,find_max_sum(root.left))
        right = max(0,find_max_sum(root.right))
        max_sum[0] = max(max_sum[0],left+right+root.data)
        return root.data + max(left,right)
    find_max_sum(root)
    return max_sum[0]  

#method 01 the method way is like level-order traversal
def check_wheather_two_graphs_are_same(p,q):
    if not q and not p: return True
    if not p or not q: return False
    q1 = [p]
    q2 = [q]
    while q1 and q2:
        if len(q1) != len(q2): return False
        n = len(q1)
        for _ in range(n):
            value1 = q1.pop(0)
            value2 = q2.pop(0)
            if value1.data != value2.data: return False
            if value1.left and value2.left: 
                q1.append(value1.left)
                q2.append(value2.left)
            else:
                if value1.left or value2.left:
                    return False
            if value1.right and value2.right:
                q1.append(value2.right)
                q2.append(value2.right)
            else:
                if value1.right or value2.right:
                    return False
    return True 

#method 02
def check_weather_two_graphs_are_same2(p,q):
    if not p and not q: return True
    elif not p or not q or p.data != q.data: return False
    else: return check_weather_two_graphs_are_same2(p.left,q.left) and check_weather_two_graphs_are_same2(p.right,q.right) 
      

root = None
# arr = [5,4,3,6,2,1,7,8,9]
arr = [10,7,12,5,8,1,6,11,15,14,17]
# arr = [5,2,3,1,7,8]
# arr = [2,1,3]
# arr = [-10,9,20,15,7]

# for i in arr:
#     root = insert(root,i)
# traversal('root',root)
# print()
# print(total_path_sum(root))
# # print(longest_diameter(root))
# print(max_sum_path(root))


p = [1,2,3]
q = [1,2,3]
root1 = None
root2 = None
for i in zip(p,q):
    root1 = insert(root1,i[0])
    root2 = insert(root2,i[-1])
# traversal('root',root1)
# traversal('root',root2)
# print(check_wheather_two_graphs_are_same(root1,root2))
# print(check_weather_two_graphs_are_same2(root1,root2))

# Graphs 📊
nodes =[ ('A', 'B'),
    ('A', 'C'),
    ('B', 'C'),
    ('B', 'D'),
    ('C', 'D'),
    ('D', 'E'),
    ('E', 'F'),
    ('F', 'C') 
]

#method 01
# graph = dict()
# for i,j in nodes:
#     if i in graph: graph[i].append(j)
#     else: graph[i] = [j]
#     if j in graph: graph[j].append(i)
#     else:graph[j] = [i]
# print(graph)

#method 02 is at the bottom page

# find the no of the paths from source to destsination 
def find_no_of_paths(graph,start,end,visited = None):
    if visited is None:
        visited = set()
        
    if start == end:
        return  1
    
    visited.add(start)
    totalpaths = 0
    for i in graph.get(start,[]): # [] list is used because for edge case because if user give invalid no which is not present in the graph it will help to avoid error
        if i not in visited:
            totalpaths += find_no_of_paths(graph,i,end,visited)
    visited.remove(start)
    return totalpaths

# minimum no of nodes to reach the other end of the graph
def min_way_to_reach_the_end(graph,start,end,visited = None,depth = 0):
    if not visited:
        visited = set()
        
    if start == end:
        return depth
    
    visited.add(start)
    mini = float("inf")
    for i in graph[start]:
        if i not in visited:
            mini = min(mini,min_way_to_reach_the_end(graph,i,end,visited,depth+1))
    visited.remove(start)
    return mini

#breadth first search

from collections import deque
def bfs(graph,start,visited):
    q= deque([start])
    visited.add(start)

    while q:
        nodes = q.popleft()
        for i in graph[nodes]:
            if i not in visited: 
                visited.add(i)
                q.append(i)
    print(visited)


# def loop_exits

       
    
    
# nodes = ((5,2),(5,7),(5,8),(2,7),(2,8),(8,7),(8,3),(2,3))

# nodes = [
#     ('A', 'B'),
#     ('A', 'C'),
#     ('B', 'D'),
#     ('B', 'E'),
#     ('C', 'F'),
#     ('D', 'F'),
#     ('E', 'F')
# ]


#cycle nodes
edges = [
    ('A', 'B'),
    ('B', 'C'),
    ('C', 'D'),
    ('D', 'B')  # cycle here
]
from collections import defaultdict
#method 02 using default dictionary for cyclic graph
graph = defaultdict(list)
for i, j in nodes:
    graph[i].append(j)
    graph[j].append(i)
print(dict(graph))
# print(find_no_of_paths(graph,'A','F'))
# print(min_way_to_reach_the_end(graph,'A','F'))
# bfs(graph,'A',set())


#weighted graph

edges = [
    ('A', 'B', 4),
    ('A', 'C', 2),
    ('B', 'C', 5),
    ('B', 'D', 10),
    ('C', 'E', 3),
    ('E', 'D', 4),
    ('D', 'F', 11)
]

graph = defaultdict(list)
for i,j,w in edges:
    graph[i].append([j,w])
    graph[j].append([i,w])  
print(graph)  

# Acyclic Graph
def count_no_of_paths(graph,start,end):
    if start == end:
        return 1
    count = 0
    for i in graph[start]:
        count += count_no_of_paths(graph,i,end)
    return count
    
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('B', 'D'),
    ('B', 'E'),
    ('C', 'F'),
    ('D', 'F'),
    ('E', 'F')
]

graph = defaultdict(list)
for i,j in edges:
    graph[i] = graph.get(i,[]) + [j]
    graph[j] = graph.get(j,[])
# print(dict(graph))
# print(count_no_of_paths(graph,'A','F'))


