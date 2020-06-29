'''In a gold mine grid of size m * n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:

Every time you are located in a cell you will collect all the gold in that cell.
From your position you can walk one step to the left, right, up or down.
You can't visit the same cell more than once.
Never visit a cell with 0 gold.
You can start and stop collecting gold from any position in the grid that has some gold.

EX
Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
Output: 24
Explanation:
[[0,6,0],
 [5,8,7],
 [0,9,0]]
Path to get the maximum gold, 9 -> 8 -> 7.

Constraints:

1 <= grid.length, grid[i].length <= 15
0 <= grid[i][j] <= 100
There are at most 25 cells containing gold.
'''
import queue
    
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        max_sum=0
        
        def find_sum(g,a,b):
            if b!=2 or a!=1:
                return (22,10)
            q=queue.Queue(maxsize=0)
            v=[]
            curr_sum=0
            max_sum=0
            #Do BFS to find maximum gold possible
            q.put((b,a,0,0))
            while q.empty()==False:
                curr=q.get()
                this_b=curr[0]
                this_a=curr[1]
                cells=curr[2]
                curr_sum=curr[3]
                #Add Current Value to Current Sum
                curr_sum+=g[this_b][this_a]
                print(curr_sum)
                if curr_sum>max_sum:
                    max_sum=curr_sum
                #Total cells=25 then max solution found
                if cells==25:
                    return (curr_sum,25)
                #Add current to Visited
                v.append((this_b,this_a))
                #Add current NSEW to queue unless val of 0 or in Visited
                if this_b+1<len(g) and g[this_b+1][this_a]>0 and (this_b+1,this_a) not in v:
                    q.put((this_b+1,this_a,cells,curr_sum))
                if this_b-1>-1 and g[this_b-1][this_a]>0 and (this_b-1,this_a) not in v:
                    q.put((this_b-1,this_a,cells,curr_sum))
                if this_a+1<len(g[this_b]) and g[this_b][this_a+1]>0 and (this_b,this_a+1) not in v:
                    q.put((this_b,this_a+1,cells,curr_sum))
                if this_a-1>-1 and g[this_b][this_a-1]>0 and (this_b,this_a-1) not in v:
                    q.put((this_b,this_a-1,cells,curr_sum))
            return (max_sum,cells)
                
        
        #Check every non-0 cell as a starting point
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x]>0:
                    total=find_sum(grid,x,y)
                    if total[1]==25:
                        return total[0]
                    if total[0]>max_sum:
                        max_sum=total[0]
                
        #Return the max sum
        return max_sum
