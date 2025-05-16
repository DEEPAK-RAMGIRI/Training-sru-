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
        
        
        
# Printing the number of islands in the matrix
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

# printng no of possible ways to reach the end 
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
# print(toend(list1,0,0))


# 0 is land 1 is tree  and we put fire on the arr[2][5] the trees which are connected are akso set on fire 
# bcoz of connection between the points

arr = [
    [1,0,0,1,1,1],
    [1,1,1,0,0,0],
    [0,0,1,1,1,1],
    [1,1,1,0,0,0],
    [0,0,0,0,0,1],
    [1,0,0,1,0,0]
] 

def burnttree(i,j):
    if i < 0 or i >= len(arr) or j < 0 or j >= len(arr[0]) or arr[i][j] == 0:
        return
    if arr[i][j] == 1:
        arr[i][j] = 0
    burnttree(i+1,j)
    burnttree(i,j+1)
    burnttree(i-1,j)
    burnttree(i,j-1)
burnttree(2,5)

count = 0
for i in arr:
    count += sum(i)
# print(f"The trees which are not burnt {count}")


#we have a box 5X5 and we have a frog that is jumping 
#here we have a condition it should not jump in the boxes (1,0),(3,0),(4,1),(2,4)
#print no of possible ways that it reach the end of the matrix
#it move right and down side only
matrix = 5
#method 01
def jump(i,j):
    if i == matrix-1 and j == matrix-1:
        return 1
    if i >= matrix or j >= matrix or (i == 1 and j == 0) or (i == 3 and j ==0) or (i == 4 and j == 1) or (i == 2 and j == 4):
        return 0
    return jump(i+1,j) + jump(i,j+1)
# print(f"Number of possible ways to the reach end: {jump(1,2)}")



# decimal to binary using recursion may be !
import math
def tobinary(string,a,n):
    if a == -1:
        return a
    if len(string) == n:
        print(string)
        a=a-1
        return a
    a = tobinary(string + '0',a,n)
    a = tobinary(string + '1',a,n)
    return a
n = 18
# tobinary("",n,int(math.log(n,2))+1)


#print parenthese
n = 3
def parenthesis(string):
    if len(string) == 2*n:
        print(string)
        return
    parenthesis(string+"(")
    parenthesis(string+')')
# parenthesis("")


#print the valid parenthesis
n = 3
def generate_parenthesis(string,left,right):
    if len(string) == 2*n:
        print(string)
        return
    if left < n:
        generate_parenthesis(string + "(",left+1,right)
    if right < left:
        generate_parenthesis(string +")",left, right+1)
    return
generate_parenthesis("",0,0)
    



     
         