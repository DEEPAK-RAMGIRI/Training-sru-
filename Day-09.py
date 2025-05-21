# arr1= [
#     [1,2,3,4],
#     [32,41,52,6],
#     [34,345,51,23],
#     [12,354,7,18]
# ]
# #method 01
# key = 345
# # for i in arr1:
# #     flag = False
# #     for j in i:
# #         if key == j:
# #             flag = True
# #             print('found')
# #             break
# #     if flag: break
# # else:
# #     print("Not found")

# #method 02
# # for i in arr1:
# #     if key in i:
# #         print('found')
# #         break
# # else:
# #     print("Not found")
    
# #method 03
# key = 345
# # if any(key in sublist for sublist in arr1):
# #     print("found")
# # else:
# #     print("Not found")
    
# # Time Complexcity o(n * log(n))
# arr = [
#     [2,3,7,8],
#     [9,15,20,22],
#     [23,26,35,37],
#     [38,39,42,43]
# ]
# # key = 23
# # found = False
# # for i in arr:
# #     left = 0
# #     right = len(i) - 1 
# #     if i[left] <= key <= i[right]:
# #         while left <= right:
# #             mid = left + ((right - left) >> 1) 
# #             if i[mid] == key:
# #                 print("found")
# #                 found = True
# #                 break
# #             elif i[mid] < key :
# #                 left = mid  + 1
# #             else:
# #                 right = mid - 1
# #     if found:
# #         break
# # if not found:
# #     print("not found")
    
# #Time Complexcity O( n + log(n))
# # found = False
# # for i in range(len(arr)):
# #     if arr[i][0] < key < arr[i][1]:
# #         break
# # else:
# #     print("not found")
# #     exit()

# left = 0
# right = len(arr[i]) - 1
# while left <= right:
#     mid = left + ((right - left) >> 1)
#     if arr[i][mid] == key:
#         # print("found")
#         found = True
#         break
#     elif arr[i][mid] < key:
#         left = mid + 1
#     else:
#         right = mid - 1

# if not found:
#     print("not found")


#Time Complexcity O(log m + logn)
arr = [
    [2,3,7,8],
    [9,15,20,22],
    [23,26,35,37],
    [38,39,42,43]
]
key = 23
left = 0
n = len(arr[0]) - 1
right = n
while left <= right:
    mid = left + ((right - left) >> 1)
    # print(arr[mid][n])
    if arr[mid][n] < key:
        left = mid + 1
    else:
        right = mid - 1

row = left
right = len(arr[left]) - 1
left = 0
while left <= right:
    mid = left +((right - left) >> 1)
    if arr[row][mid] == key:
        # print("found")
        break
    elif arr[row][mid] < key:
        left = mid + 1
        
    else:
        right = mid -1
        
# else:
#     print("not found")


# method 03 More optimised method 
# log n * m
arr = [
    [2, 3, 7, 8],
    [9, 15, 20, 22],
    [23, 26, 35, 37],
    [38, 39, 42, 43]
]
key = 23

n = len(arr)       # number of rows
m = len(arr[0])    # number of columns

left = 0
right = n * m - 1

found = False
while left <= right:
    mid = left + ((right - left) >> 1)
    row = mid // m
    col = mid % m
    if arr[row][col] == key:
        # print("Found at position:", (row, col))
        found = True
        break
    elif key < arr[row][col]:
        right = mid - 1
    else:
        left = mid + 1

if not found:
    print("Not found")

# here in this in each array values are increasing
# here consider top right element as mid  
arr =[
    [3,4,6,8],
    [5,7,9,10],
    [8,12,13,15],
    [20,23,26,28],
    [30,36,40,45]
]

key = 23
right = len(arr[0])-1
left = 0
while left < len(arr) and right >= 0:
    print(arr[left][right])
    if arr[left][right] == key:
        print("found")
        break
    elif arr[left][right] > key:
        right-=1
    else:
        left+=1
else:
    print("not found")

