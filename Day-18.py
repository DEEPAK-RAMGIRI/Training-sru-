from collections import defaultdict,deque
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def create_graph(self,edges):
        for i,j in edges:
            self.graph[i].append(j)
            self.graph[j].append(i)
        
    
    def print_graph(self):
        print(dict(self.graph))
        
    def bfs_breadth_first_search(self,start):
        queue = deque([start])
        visit = set()
        ans = []
        visit.add(start)
        ans.append(start)
        while queue:
            nodes = queue.popleft()
            for i in self.graph[nodes]:
                if i not in visit:
                    ans.append(i)
                    queue.append(i)
                    visit.add(i)
        return ans
            
        
        
    def dfs_depth_first_search(self,visit,start,final):
        visit.add(start)
        final.append(start)
        for i in self.graph[start]:
            if i not in visit:
                self.dfs_depth_first_search (visit,i,final)
                
        return final
        
        
        
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('B', 'D'),
    ('B', 'E'),
    ('C', 'F'),
    ('D', 'F'),
    ('E', 'F')
]
G = Graph()
# G.create_graph(edges)
# G.print_graph()
# print(G.dfs_depth_first_search({edges[0][0]},edges[0][0],[]))
# print(G.bfs_breadth_first_search(edges[0][0]))


import heapq

def dijkstra(graph,start):
    #Assigning infinte to all present nodes in the edges
    distance = {i: float("inf") for i in graph}
    distance[start] = 0
    queue = [(0,start)]
    while queue:
        dis,node  = heapq.heappop(queue)
        for nod,wei in graph[node]:
            
            new  = dis + wei
            if new < distance[nod]:
                distance[nod] = new
                heapq.heappush(queue,(distance[nod],nod))
            
    return distance
                
    

    
edges = [
    (10, 5, 2),
    (10, 7, 4),
    (5, 3, 2),
    (5, 7, 1),
    (5, 8, 3),
    (7, 8, 1),
    (8 ,3,1)
]

graph = defaultdict(list)
for i,j,w in edges:
    graph[i].append([j,w])
    graph[j].append([i,w])  
# print(dict(graph))
print(dijkstra(graph,10))


for i in range(10):
    if i ==4:
        continue
    print(i)
    print("hello")