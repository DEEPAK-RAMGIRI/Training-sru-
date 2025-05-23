arr1 = [0,3,8,1,5,7,9]
arr2 = [5,6,10,2,6,9,11]

 
# finding the possible max intervals 
time_intervals = []

i= 0
while i < len(arr1):
    time_intervals.append([arr1[i],arr2[i]])
    i+=1
#instead of while loop use zip
#here it will convert to tuple instead of use list bcoz tuple is immutable
# for i in zip(arr1,arr2):
#     time_intervals.append(i)

time_intervals.sort(key = lambda x:(x[-1],x[0])) # sorting the time_intervals values
print(time_intervals)
count = 1
last = time_intervals[0]

for i in range(1,len(time_intervals)):
    if last[-1] < time_intervals[i][0]:
        # print(last,end=" ")
        last = time_intervals[i]
        count+=1
        
# print(last,end=" ")
# print(count)

#merging intervals
ans = []
ans.append(time_intervals[0])
for i in range(1,len(time_intervals)):
    if ans[-1][-1] > time_intervals[i][0]:
        ans[-1][0] = min(ans[-1][0],time_intervals[i][0])
        ans[-1][-1]= max(ans[-1][0],time_intervals[i][-1])
    else:
        ans.append(time_intervals[i])
# print(ans)



# string = "aaabbaaaacccddeff"
# string="abbacbababc"
# left = 0
# for right in range(1,len(string)):
#     if string[right] != string[right-1]:
#         print(string[right-1],right-left,end=" ")
#         left = right
# print(string[right],len(string)-left,end=" ")

#reverse the string without changing the vowels but u can change the vowels

string = "hippopotamus"
string = list(string)
vowels = "aeiou"
left = 0
right = len(string) -1
while left < right:
    while left < right and string[left] in vowels:
        left+=1
    while left < right and string[right] in vowels:
        right-=1
    string[left],string[right] = string[right],string[left]
    left+=1
    right-=1
# print(''.join(string))
    
    
# i am visting a library 
arr = [2,1,6,4,2,3,1,1,4,2,6,7,3]
k = 5
maxi = sum(arr[:k])
ans = maxi
left = 0
for right in range(k,len(arr)):
    maxi +=  (arr[right]-arr[left])
    left+=1
    ans= max(maxi,ans)
print(ans)
    