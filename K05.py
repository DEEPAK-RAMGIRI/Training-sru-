from collections import defaultdict,deque

edges = [
    [2,4],
    [2,5],
    [2,6],
    [5,6],
    [4,6],
    [4,7],
    [6,7]
] 

graph = defaultdict(list)
for i,j in edges:
    graph[i].append(j)
    graph[j].append(i)

key = 6
visit = set()
def BFS(root,key):
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node == key: return True
        visit.add(node)
        for i in graph[node]:
            if i not in visit:
              queue.append(i)  
    return False

def DFS(node,key):
    visit.add(node)
    if node == key: return True
    for i in graph[node]:
        if i not in visit:
            if DFS(i,key):
                return True
    return False
    
    
edges = [[2,7],[2,1],[7,1],[7,6],[5,3],[5,9],[4,8],[9,3]]

graph = defaultdict(list)
for i,j in edges:
    graph[i].append(j)
    graph[j].append(i)

visit = set()
def DFS(node):
    visit.add(node)
    sums = node
    for i in graph[node]:
        if i not in visit:
            sums +=  DFS(i)
    return sums
maxi = 0
for i in graph.keys():
    if i not in visit:
        maxi  = max(maxi,DFS(i))
print(maxi)
    

    