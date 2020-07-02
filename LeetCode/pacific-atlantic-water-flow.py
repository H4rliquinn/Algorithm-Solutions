'''Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.
Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.
Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:
The order of returned grid coordinates does not matter.
Both m and n are less than 150.
 
Example:
Given the following 5x5 matrix:
  Pacific ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:
[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
'''
import queue
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        
       
        ans=[]
        for x in range(len(matrix)):
            ans.append([])
            for y in matrix[0]:
                ans[x].append((0,0))
        q=queue.Queue(maxsize=0)
        rtn=[]
        
        #Set Pacific possible
        for x in range(len(matrix[0])):
            ans[0][x]=(1,0)
            q.put((0,x))
        for x in range(1,len(matrix)):
            ans[x][0]=(1,0)
            q.put((x,0)) 
        while q.empty()==False:

            curr=q.get()
            if curr[0]+1>len(matrix)-1:
                ans[curr[0]][curr[1]]=(1,1)
            elif ans[curr[0]+1][curr[1]][0]<1:
                if matrix[curr[0]+1][curr[1]]>=matrix[curr[0]][curr[1]]:
                    q.put((curr[0]+1,curr[1]))
                    ans[curr[0]+1][curr[1]]=(1,0)
                else:
                    if ans[curr[0]+1][curr[1]][0]!=1:
                        ans[curr[0]+1][curr[1]]=(-1,0)
                        
            if curr[1]+1>len(matrix[0])-1:
                ans[curr[0]][curr[1]]=(1,1)        
            elif ans[curr[0]][curr[1]+1][0]<1:
                if matrix[curr[0]][curr[1]+1]>=matrix[curr[0]][curr[1]]:
                    q.put((curr[0],curr[1]+1))
                    ans[curr[0]][curr[1]+1]=(1,0)
                else:
                    if ans[curr[0]][curr[1]+1][0]!=1:
                        ans[curr[0]][curr[1]+1]=(-1,0)   
                        
        #Set Atlantic possible
        
        for x in range(len(matrix[0])):
            ans[len(matrix)-1][x]=(ans[len(matrix)-1][x][0],1)
            q.put((len(matrix)-1,x))    
        for x in range(len(matrix)-1):
            ans[x][len(matrix[0])-1]=(ans[x][len(matrix[0])-1][0],1)
            q.put((x,len(matrix[0])-1))
 
#         while q.empty()==False:
#             curr=q.get()
#             if curr[0]+1>len(matrix)-1:
#                 ans[curr[0]][curr[1]]=(1,1)
#             elif ans[curr[0]+1][curr[1]][0]<1:
#                 if matrix[curr[0]+1][curr[1]]>=matrix[curr[0]][curr[1]]:
#                     q.put((curr[0]+1,curr[1]))
#                     ans[curr[0]+1][curr[1]]=(1,0)
#                 else:
#                     if ans[curr[0]+1][curr[1]][0]!=1:
#                         ans[curr[0]+1][curr[1]]=(-1,0)
                        
#             if curr[1]+1>len(matrix[0])-1:
#                 ans[curr[0]][curr[1]]=(1,1)        
#             elif ans[curr[0]][curr[1]+1][0]<1:
#                 if matrix[curr[0]][curr[1]+1]>=matrix[curr[0]][curr[1]]:
#                     q.put((curr[0],curr[1]+1))
#                     ans[curr[0]][curr[1]+1]=(1,0)
#                 else:
#                     if ans[curr[0]][curr[1]+1][0]!=1:
#                         ans[curr[0]][curr[1]+1]=(-1,0)        
        
        #Find answer
        
        print("QUEUE",list(q.queue))        
        print("ANSWER")
        for x in ans:
            print(x)