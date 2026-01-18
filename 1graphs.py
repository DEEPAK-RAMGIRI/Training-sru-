edges = [
    [1,2],
    [1,3],
    [3,4],
    [2,4],
    [4,5],
    [2,5]   
]

n = 5
from collections import defaultdict,deque
Graph = defaultdict(list)
for i,j in edges:
    Graph[i].append(j)
    Graph[j].append(i)


# BFS
def BFS():
    visit = [False] * (n  + 1)
    queue = deque([1])
    visit[1] = True  # visit must be here
    while queue:
        node= queue.popleft()
        print(node)
        for i in Graph[node]:
            if not visit[i]:
                visit[i] = True # visit must be here and also here
                queue.append(i)
# BFS()
visit = [False] * (n  + 1)
def DFS(root):
    visit[root] = True 
    for i in Graph[root]:
        if not visit[i]:
            DFS(i)
    
def no_of_provinces():
    edges = [
        [1,0,1],
        [0,1,0],
        [1,0,1]
    ]
    
    visit = [False] * len(edges)


    def dfs(root):
        visit[root] = True
        for i in range(len(edges[root])):
            if edges[root][i] == 1 and not visit[i]:
                dfs(i)
        return 1
    
    count = 0
    for i in range(len(visit)):
        if not visit[i]:
            count += dfs(i)
    print(count)
# no_of_provinces()


def flood_fill():
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1
    sc = 1
    color = 2
    source = image[sr][sc]
    queue = deque([(sr,sc)])
    image[sr][sc] = color
    while queue:
        x,y = queue.popleft()
        for i,j in [(-1,0),(1,0),(0,-1),(0,1)]:
            if 0 <= i + x < len(image) and 0 <= j + y < len(image[0]) and image[i + x][j + y] == source:
                queue.append((i + x,j + y))
                image[i + x][j + y] = color
                
               
def rotten():
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    queue = deque()
    fresh = 0
    time = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 2:
                queue.append((i,j,0))
            elif grid[i][j] == 1:
                fresh += 1
    
    while queue:
        x,y,t  = queue.popleft()
        time = max(t,time)
        for i,j in [(-1,0),(1,0),(0,-1),(0,1)]:
            if 0 <= x + i < len(grid) and 0 <= j + y < len(grid[0]) and grid[i + x][j + y] == 1:
                queue.append((i + x, j  + y , t + 1))
                grid[i + x][j + y] = 2
                fresh-=1
                
    if fresh: return -1
    return time


edges = [[1,2],[1,3],[2,5],[5,7],[3,6],[3,4],[6,7]]
graph = defaultdict(list)
for i,j in edges:
    graph[i].append(j)
    graph[j].append(i)  
visit = [False] * (len(edges) + 1)
def cycle_in_graph():
    queue = deque([(1,-1)])
    visit[1] = True
    while queue:
        node,parent = queue.popleft()
        for i in graph[node]:
            if visit[i] and parent != i:
                return True
            if not visit[i]:
                visit[i] = True
                queue.append((i,node))
    return False
# print(cycle_in_graph())             

visit = [False] * (len(edges) + 1)
def cycle_of_graph(root,parent):
    visit[root] = True
    for i in graph[root]:
        if visit[i] and parent != i:
            return True
        if not visit[i]:
            if cycle_of_graph(i,root):
                return True
    return False        
# print(cycle_of_graph(1,-1))

def nearest_cell():
    matrix = [
        [0,0,0],
        [0,1,0],
        [1,1,1]
    ]

    visit = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    dist  = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

    queue = deque([])
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                visit[i][j] = False
                queue.append((i,j,0))

    while queue:
        x,y,step = queue.popleft()
        dist[x][y] = step
        for i,j in [(0,1),(0,-1),(-1,0),(1,0)]:
            if  0 <= i + x < len(matrix) and 0 <= j + y < len(matrix[0]) and not visit[i + x][j + y]and matrix[i + x][j + y] == 1:
                visit[x + i][j + y] = True
                queue.append((i + x,j + y,step + 1))
    # print(dist)
        
# nearest_cell()

# detect cycle in the directed graph
def cycle():
    edges = [ [1,2], [2,3], [3,4], [3,7], [4,5], [5,6], [7,5],[8,9], [9,10], [10,8]]

    graph = defaultdict(list)
    for i,j in edges:
        graph[i].append(j)
        
    visit = [False] * 11
    path_visit = [False] * 11
    def dfs(root):
        visit[root] = True
        path_visit[root] = True
        for i in graph[root]:
            if not visit[i]:
                if dfs(i): return True
            elif path_visit[i]:
                return True
        path_visit[root] = False
        return False
            
    for i in range(1,11):
        if not visit[i]:
            if dfs(i):
                return True
    return False

from collections import deque, defaultdict

def kahn_topo(n, edges):
    graph = defaultdict(list)
    indegree = [0] * n

    # build graph & indegree
    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1

    q = deque()
    for i in range(n):
        if indegree[i] == 0:
            q.append(i)

    topo = []
    while q:
        node = q.popleft()
        topo.append(node)

        for nei in graph[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)

 
    if len(topo) != n:
        return "Cycle detected"

    return topo

n = 6
edges = [(5,2),(5,0),(4,0),(4,1),(2,3),(3,1)]
# print(kahn_topo(n, edges))

# print(cycle())


def isBipartite(self, graph):  
    colors = [-1] * len(graph)
    def bfs(root):
        queue = deque([root])
        colors[root] = 0
        while queue:
            node = queue.popleft()
            for i in graph[node]:
                if colors[i] == -1:
                    colors[i] = 0 if colors[node] else 1
                    queue.append(i)
                elif colors[i] == colors[node]:
                    return False
        return True

    for i in range(len(graph)):
        if colors[i] == -1:
            if not bfs(i):
                return False
    return True

import heapq
def dijkstra():
    edges = [
        [0,1,4],
        [0,2,4],
        [1,2,2],
        [2,3,3],
        [2,4,1],
        [2,5,6],
        [3,5,2],
        [4,5,3]
    ]
    
    graph = defaultdict(list)
    
    for i,j,k in edges:
        graph[i].append((j,k))
        graph[j].append((i,k))
    
    dist = [0] +[float("inf")] * 5
    
    queue = []
    heapq.heappush(queue,(0,0))
    while queue:
        dis,node = heapq.heappop(queue)
        for nod,di in graph[node]:
            if di + dis < dist[nod]:
                dist[nod] = di + dis
                queue.append((di + dis,nod))
    return dist
print(dijkstra())