string = "abcdecfbgce"

string = "abcdaecdb"
# string ="abcdbef"
# string ="abcda"
# string = "abfehcbdaf"
# string = "abcdcecdb"
# string = "abcdcecda"

#Time complexcit is O(n)

left = 0
seen =dict()
maxi = 0
for right in range(len(string)):
    if string[right] in seen:
        left = max(left,seen[string[right]])
    seen[string[right]] = right
    maxi = max(maxi,right - left)
# print(maxi)


# print the longest substring which have m,n
string = "abcdedacefaebg"
m,n = 'c','d'

left = 0
seen =dict()
maxi = 0
for right in range(len(string)):
    if string[right] in seen:
        left = max(left,seen[string[right]])
    seen[string[right]] = right
    if m in seen and n in seen:
        maxi = max(maxi,right - left)
# print(maxi)

#print the maximum sum after removing the values either from top or bottom so the sum of list1 must be greater
list1 = [4,2,7,20,8,60,4,1]
front = 0
last = len(list1) - 1
k = 3
while front < last and k > 0:
    if list1[front] == list1[last]:
        f = front
        l = last
        while f< l and list1[f] == list1[l]:
            f+=1
            l-=1
        front += 1 if list1[f] < list1[l] else 0
        last -= 1 if list1[f] >= list1[l] else 0
        
    elif  list1[front] < list1[last]:
        front+=1
    else:
        last-=1
    k-=1
# print(front,last)
# print(sum(list1[front:last+1]))

#method 01
#print the maximum pick from the list1 here we can either pick it from fron tor back
list1 = [4,2,67,20,8,60,8,7]
# list1 = [1,2,5,2,3,4,45,23,5,6,6,7,1,1] 
list1=[4,3,2,5,6,1,12,3]
list1 =[4,3,2,5,6,1,12,3]
k= 4
ans = maxi = sum(list1[:k])
# Time Complexcity O(k)
# Space Complexcity O(1)
for i in range(k):
    # print(maxi,list1[~i+k],list1[~i])
    maxi = (maxi - list1[~i+k]) + list1[~i]
    ans = max(maxi,ans)
# print(ans)


#Fruit Into Baskets
#Time Complexcity O(n)
def totalFruit(fruits):
    seen = dict()
    left = 0
    count = 0
    for right in range(len(fruits)):
        seen[fruits[right]] = seen.get(fruits[right],0)+1
        while len(seen) > 2:
            seen[fruits[left]] = seen.get(fruits[left],0)-1
            if seen[fruits[left]] == 0:
                del seen[fruits[left]]
            left+=1
        count = max(count,right - left + 1)
    return count
# print(totalFruit([3,3,3,1,2,1,1,2,3,3,4]))

a = [900, 945, 1110, 1230, 1235, 1245, 1340, 1700]
b = [930, 1130, 1120, 1250, 1250, 1415, 1400, 1730]


# while i < len(a):
#     if a[i] < b[j]:
#         doctors += 1
#         max_doctors = max(max_doctors, doctors)
#         i += 1
#     else:
#         doctors -= 1
#         j += 1
# print("Minimum number of doctors required:", max_doctors)


doctors = 0
max_doctors = 1
i = 1
j = 0 
while i< len(a) and j < len(b):
    if a[i] < b[j]:
        doctors+=1
        max_doctors = max(max_doctors,doctors)
    else:
        doctors-=1
    i+=1
    j+=1
print(max_doctors)
        
        
    