# Time Complexcity O(3^n)
# Space Complexcity O(1)
def recursion(n,count):
    if n == 1:return count
    elif n <=0: return float("inf")
    return min(recursion(n - 1,count + 1), recursion(n //2,count + 1), recursion(n - (2 * n) // 3, count + 1))

# print("recursion" , recursion(5,0))
# print("recursion" , recursion(6,0))
# print("recursion" , recursion(1,0))


n = 5
n = 6
n = 1
dp  = [-1] * (n+1)
def Dynamic_prog(n):
    if n == 1: return 0
    elif n <= 0: return float("inf")
    elif dp[n] != -1: return dp[n]
    else:
        dp[n] = 1 + min(Dynamic_prog(n-1),Dynamic_prog(n//2),Dynamic_prog(n // 3))
        return dp[n]
# print(Dynamic_prog(n))


arr = [['A','E'],
['E','E']]

arr =[['A','E'],
 ['*','*'],
 ['E','E']
 ]

arr = [['A','E'], ['*','E'], ['E','E']]
countE = 0
from collections import deque
queue = deque()
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j] == 'E':countE+=1
        elif arr[i][j] == 'A':
            queue.append(([i,j,0]))
            
list1 = [(0,1),(0,-1),(1,0),(-1,0)]   
maxi = 0     
while queue:
    i,j,t = queue.popleft()
    maxi= max(maxi,t)
    for x,y in list1:
        if 0 <= x+i < len(arr)  and 0 <= j+y < len(arr[0]) and arr[i+x][j+y] == 'E':
            queue.append(([(i+x),(j+y),t+1]))
            arr[i+x][j+y] = 'A'
            countE-=1
# print(maxi if not countE else -1)


A = [0, 2, 1, 1]
# A = [0, 1, 2, 1, 0]
A = [0, 1, 0, 1, 1, 0, 3, 2, 1, 0]
A= [0, 2, 1, 1]
A=[0, 1, 2, 1, 0]
A=[0, 1, 0, 1, 1, 0, 3, 2, 1, 0]
A = [0, 1, 2, 4, 3]
A = [0, 1, 2, 3, 3, 4]

final = 1
sets = set()
teams = []
for i in range(len(A)):
    if A[i] in sets:
        teams.append(list(sets))
        sets.clear()
    sets.add(A[i])
teams.append(list(sets))

total = 0
for i in teams:
    wex = 0
    while wex in i:
        wex+=1
    total+=wex
# print(total)    
        
        
#Dijkstra algorithm

edges = [
    [0,1,4],
    [0,2,4],
    [1,2,2],
    [2,3,3],
    [2,4,1],
    [2,5,6],
    [3,5,2],
    [4,5,3],
]

from collections import defaultdict
graph = defaultdict(list)
for i,j,k in edges:
    graph[i].append([j,k])
    graph[j].append([i,k])
# print(graph)    
        
        
# we can use priority queue and set
import heapq
dist = [0] + [float("inf")] * (len(graph) - 1)
queue = [(0,0)]

while queue:
    j,i = heapq.heappop(queue)
    if j >= dist[i]:
        continue
    dist[i] = j
    for node,weight in graph[i]:
        if dist[node] > weight + j:
            heapq.heappush(queue,(weight + j,node))
print(dist)
        
        
