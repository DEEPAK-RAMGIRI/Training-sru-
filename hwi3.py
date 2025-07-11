#Djikstra's algorithm

from collections import defaultdict
import heapq

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
maxi= 0
for i,j,k in edges:
    graph[i].append([j,k])
    graph[j].append([i,k])
    maxi = max(maxi,i,j)
# print(dict(graph))

queue = [(0,0)]
distance = [0]+[float("inf")] * (maxi)
while queue:
    weight,node = heapq.heappop(queue)
    for nextnode,nodeweight in graph[node]:
        if nodeweight + weight < distance[nextnode]:
            distance[nextnode] = nodeweight + weight 
            heapq.heappush(queue,(nodeweight + weight,nextnode))
# print(distance) 


#Topological sort

edges = [
    [5,0],
    [5,2],
    [4,0],
    [4,1],
    [2,3],
    [3,1]
]

from collections import defaultdict

graph = defaultdict(list)

visited = [False] * 6
stack = []
def dfs(node):
    for i in graph[node]:
        if not visited[i]:
            visited[i] = True
            dfs(i)
    stack.append(node)
    
    
for i,j in edges:
    graph[i].append(j)
    
for i in range(6):  
    if not visited[i]:
        visited[i] = True
        dfs(i)
        
print(stack[::-1])






