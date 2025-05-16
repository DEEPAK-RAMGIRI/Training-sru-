#an array of integers contain duplicatees and unique find the max profit
#Greedy algorithm
arr = [3,4,2,5,8,1,4]
day = arr[0]
profit = 0
for i in range(1,len(arr)):
    if day > arr[i]:
        day = arr[i]
    profit = max(profit,arr[i]-day)
# print(profit)  
#Time Complexcity O(n)




list1 = [
    [1,0,0,1,1],
    [1,0,0,0,1],
    [0,0,0,0,0],
    [1,0,0,0,0],
    [1,0,0,0,1]
]

code = [7,6,5,2,1]
marks =[]
for i in list1:
    sums = 0
    for j in range(len(i)):
        if i[j]:
            sums += code[j]
    marks.append(sums)
    
# print(marks)
        
# Printing the island methos
visted = [[False for _ in range(len(list1[0]))] for _ in range(len(list1))]
def island(list1, i, j):
    if i < 0 or i >= len(list1) or j >= len(list1[0]) or j < 0:
        return 0
    if list1[i][j] == 0 or visted[i][j]:
        return 0
    visted[i][j] = True
    island(list1,i+1,j)
    island(list1,i,j+1)
    island(list1,i-1,j)
    island(list1,i,j-1)
    return 1

def reachout(list1):
    count = 0
    for i in range(len(list1)):
        for j in range(len(list1[0])):
            if not visted[i][j]:
                count += island(list1,i,j)
    return count
    
# print(reachout(list1))

# printng no of posiible ways to reach the end
list1 = [
    [1,0,0,0,0],
    [1,1,1,1,1],
    [1,0,1,0,1],
    [1,1,1,1,1],
    [1,1,1,0,1]
]

def toend(list1,i,j):
    if i == len(list1)-1 and j == len(list1[0])-1:
        return 1
    if i >= len(list1) or j >= len(list1[0]) or not list1[i][j]:
        return 0
    return toend(list1, i, j + 1) + toend(list1, i + 1, j)
print(toend(list1,0,0))

     
         