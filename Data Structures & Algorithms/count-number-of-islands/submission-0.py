class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def isInBounds(x , y):
            return y < len(grid) and y >= 0 and x >=0 and x < len(grid[y])
             
        def floodfill( x, y ):
            
            if isInBounds(x,y):

                if grid[y][x] == "0": 
                    return

                grid[y][x] = "0"
                floodfill(x+1,y)
                floodfill(x,y+1)
                floodfill(x-1,y)
                floodfill(x,y-1)

        islands = 0
        for y,row in enumerate(grid):
            for x,p in enumerate(row):
                if p == "1":
                    floodfill(x,y)
                    islands +=1
        return islands

    




        