matrix = [
    [1, 0, 1, 0, 0],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0]
]


for i in range(1,len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i-1][j] > 0:
            matrix[i][j]+= matrix[i-1][j]

final = matrix[-1]
total = final[0]
for i in range(len(final)):
    maxi = final[i]
    for j in range(i+1,len(final)):
        maxi = min(final[j],maxi)
        total = max(total, (j - i + 1)*maxi)
print(total) 
        
        
        
        
    