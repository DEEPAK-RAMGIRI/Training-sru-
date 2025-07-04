# Flood Fill
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2



# BFS
from collections import deque
def floodFill_BFS(image, sr, sc, color):
    if image[sr][sc] == color: return image
    source = image[sr][sc]
    list1 = [(1,0),(-1,0),(0,1),(0,-1)]
    queue = deque([(sr,sc)])
    while queue:
        i,j = queue.popleft()
        image[i][j] = color
        for x,y in list1:
            if i+x >= 0 and j+y >= 0 and i+x < len(image) and j+y < len(image[0]) and image[i+x][j+y] == source:
                queue.append(((i+x,j+y)))
    return image

#Time Complexcity O(m * n)
#because in the worst case it will color all the elements in the matrix
#Space Complexcity O(m * n)  
#in the worst we remodifying all the elements in the matrix so, O(m *n)
print(floodFill_BFS(image,sr,sc,color))



def floodFill_DFS(self, image, sr, sc, color):
    list1 = [(0,1),(1,0),(-1,0),(0,-1)] 
    def find(i,j,source):
        if i < 0 or j < 0 or i >= len(image) or j >= len(image[0]) or image[i][j] == color or image[i][j] != source:
            return 
        image[i][j] = color
        for x,y in list1:
            find(i+x,j+y,source)
        return
    find(sr,sc,image[sr][sc])
    return image

#Time Complexcity O( m*n)
#Space complexcity O(m * n)

print(floodFill_DFS(image,sr,sc,color))
        
        

            
        