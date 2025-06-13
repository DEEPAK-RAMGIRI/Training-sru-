questions = ['RGBB','RGGGGGRB','RRGGGBBBBBBBBBB','BGR']

#Time Complexcity is O(n) becoz groups take O(3) and which is O(1)
#so time Complexcity is O(n)
#Space Complexcity is O(1)

ans = []
for j in questions: #this loop for questions didn't include in time complexcity
    for i in range(len(j) - 2):
        groups = j[i:i+3]
        if set(groups) == {'R','G','B'}:
            ans.append("blackandwhite")
            break
    else:ans.append('colorful')
# print(ans)

ans = []
# Optimised version 🔥
for string in questions:
    for i in range(len(string)-2):
        a,b,c = string[i],string[i+1],string[i+2]
        if ( 'R' in (a,b,c) and 'G' in (a,b,c) and 'B' in (a,b,c)):
            ans.append('blackandwhite')
            break
    else:ans.append('colorful')
print(ans)
    