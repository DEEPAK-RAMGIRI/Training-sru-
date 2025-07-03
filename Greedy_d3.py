# Insert Interval

intervals = [[1,3],[6,9]]
newInterval = [2,5]
#Time Complexcity O( n log n)
#Space Complexcity O(n)
intervals.extend([newInterval])
intervals.sort()
arr = [intervals[0]]
for i in range(1,len(intervals)):
    if arr[-1][-1] >= intervals[i][0]:
        arr[-1] = [min(arr[-1][0],intervals[i][0]),max(arr[-1][-1],intervals[i][-1])]
    else: arr.append(intervals[i]) 
# print(arr)

# Non-overlapping Intervals

#Time Complexcity O(n log n)
#space Complexcity O(1)
intervals = [[1,2],[2,3],[3,4],[1,3]]
count = 1
intervals.sort(key = lambda x:x[-1])
prev = intervals[0][-1]
for i in range(1,len(intervals)):
    if prev <= intervals[i][0]:
        prev = intervals[i][-1]
        count+=1
# print(len(intervals) - count)


#graphs
#way 01 representation
n = 5
m = 6
arr = [[0 for _ in range(n+1)] for _ in range(n + 1)]

edges = [[1,2],
         [1,3],
         [2,4],
         [3,4],
         [3,5],
         [4,5]]

#Time Complexcity O(m)
#Space Complexcity O(n^2)
for i,j in edges:
    arr[i][j] = 1
    arr[j][i] = 1
# print(arr)

#adjancy list

from collections import defaultdict
adjlist = defaultdict(list)
#Time Complexcity O(m)
#Space complexcity O(n + m)
for i,j in edges:
    adjlist[i].append(j)
    adjlist[j].append(i)
# print(adjlist)



#for weighted graph
#using matrix
n = 5 
m = 6
edges = [[1,2,2],
         [1,3,3],
         [2,4,1],
         [3,4,4],
         [3,5,3],
         [4,5,4]
        ]

wt_graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
# Time Complexcity O(m)
#Space Complexcity O(n^2)
for i,j,k in edges:
    arr[i][j] = k
    arr[j][i] = k

# print(arr)  

#Time Complexcity O(m)
#Space Complexcity O(m + n)
from collections import defaultdict
adjlist = defaultdict(list)
for i,j,k in edges:
    adjlist[i].append((j,k))
    adjlist[j].append((i,k))
# print(adjlist)


#connected components
edges = [
    [1,2],
    [1,3],
    [2,4],
    [3,4],
    [5,6],
    [6,7],
    [5,7],
    [8,9],
    [10,10]
]

from collections import defaultdict
graph = defaultdict(list)
maxi = 0
for i,j in edges:
    graph[i].append(j)
    graph[j].append(i)
    maxi = max(i,j,maxi)
    
#dfs
#Time Complexcity O(n + m)
#Space Complexcity O(m+n)
visit = [True] + [False] * (maxi)
def dfs(i):
    visit[i] = True
    for j in graph[i]:
        if not visit[j]:
            dfs(j)
    return 1
#bfs

visit = [True] + [False] * (maxi)
#Time Complexcity O(n + m)
#Space Complexcity O(n + m)
from collections import deque
def bfs(i):
    queue = deque([i])
    visit[i] = True
    while queue:
        value = queue.popleft()
        for j in graph[value]:
            if not visit[j]:
                visit[j] = True
                queue.append(j)
    return 1

count = 0
for i in range(1,maxi+1):
    if not visit[i]:
        # count += dfs(i)
        count += bfs(i)
# print(count)

    
    

    
    

    