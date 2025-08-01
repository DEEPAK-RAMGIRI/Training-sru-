from collections import deque

edges = [
    
    [0,1],
    [2,0],
    [3,0],
    [1,3],
    [1,2]
]
n =  3

graph = [[0 for _ in range(n + 1)] for _ in range(n  + 1)]
for i,j in edges:
    graph[i][j] = 1
    
# BFS

visit = [False] * (n+1)
def BFS(index):
    queue = deque([index])
    visit[index] = True
    while queue:
        index =queue.popleft()
        print(index)
        for i in range(len(graph[index])):
            if graph[index][i] == 1 and not visit[i]:
                queue.append(i)
                visit[i] = True
# BFS(0)


# give a node print the k nodes from the root node



from collections import defaultdict

class DAG:
    def __init__(self):
        self.graph = defaultdict(list)
        
        
    def getindegreesvertices(self):
        pass
        
    
    def isvaliddependencygraph(self):
        pass
    
    def topologicalsort(self):
        stack = []

        def sorting(index):
            for i in self.graph[index]:
                sorting(i)
            stack.append(index)
        
    def getZeroindegreeVertices(self):
        pass