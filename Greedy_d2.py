#no of required trains in the railways station

#Time Complexcity O(n^2)
#Space Complexcity O(n^2)
start = [900, 945 ,955,1100,1500,1800]
end= [920,1200,1130,1150,1900,2000]

trains= []
for i in zip(start,end):
    trains.append(i)
trains.sort(key = lambda x: x[0])

times = [[] for _ in range(len(trains))]

for i in trains:
    for j in times:
        if not j:
            j.extend(list(i))
            break
        elif j[-1] <= i[0]:
            j.extend(list(i))
            break
count = 0
for i in times:
    if i:
        count+=1
# print(count)

#optimised version
#Time Complexcity O(n^2)
#Space Complexcity O(1)

start = [900, 945 ,955,1100,1500,1800]
end= [920,1200,1130,1150,1900,2000]

maxi = 0
for i in range(len(start)):
    count = 1
    for j in range(i+1,len(start)):
        if end[i] > start[j]:
            count+=1
    maxi = max(count,maxi)
# print(maxi)


#Time Complexcity O(n  log n)
#Spae Complexcity O(1)
start = [900, 945 ,955,1100,1500,1800]
end= [920,1200,1130,1150,1900,2000]


start.sort()
end.sort()
i = 0
j = 0
maxi = 0
count = 0
while i < len(start) and j < len(end):
    if start[i] < end[j]:
        count+=1
        i+=1
    else:
        j+=1
        count-=1
    maxi = max(count,maxi)
# print(maxi)


# job sequence problem

id = [1,2,3,4]
deadline = [4,1,1,1]
profit = [40,10,40,30]


# id = [6,3,4,2,5,8,1,7]
# deadline = [2,6,6,5,4,2,4,2]
# profit = [80,70,65,60,25,22,20,10]

jobs = []
for i in zip(deadline,profit):
    jobs.append(i)
jobs.sort(key= lambda x:x[-1],reverse=True)


slots = [-1] * max(deadline)
total = 0
for i,j in jobs:
    i-=1
    # print(i,j)
    while slots[i] != -1 and i >= 0:
        i-=1
    if i < 0: continue
    slots[i] = i
    total += j
# print(total)

#Candy
rate = [29,51,87,87,72,12]
# rate = [1,2,3,1,0] 

left = [1] * len(rate)
right = [1] * len(rate)

for i in range(1,len(rate)):
    if rate[i]  > rate[i - 1]:
        left[i] = left[i - 1] + 1

for i in range(len(rate)-2,-1,-1):
    if rate[i] > rate[i+1]:
        right[i] = right[i+1] +1
total = 0
for i in range(len(rate)):
    total += max(left[i],right[i])
# print(total)



#Time Complexcity O(n)
#Space Complexcity O(2)

rate = [29,51,87,87,72,12]
rate = [1,2,3,1,0]

i = 1
sums = 1

while i < len(rate):
    if rate[i] == rate[i - 1]:
        sums+=1
        i+=1
    peak = 1
    while i < len(rate) and rate[i] > rate[i-1]:
        peak+=1
        sums += peak
        i+=1
    down = 1
    while i < len(rate) and rate[i] < rate[i -1]:
        down+=1
        sums+=down
        i+=1
    sums += (down - peak) if down > peak else 0
    
# print(sums) 
        
        
        
#Shortest Job First

#Time Complexcity O(n log n)
#Space Comnplexcity O(1)
jobs = [4,3,7,1,2]
jobs.sort()
waiting = total = 0
for i in jobs:
    total += waiting
    waiting += i
print(total // len(jobs))
    
    