class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

             
        def floodfill( x, y ):
            
            grid[y][x] = "0"
            if y + 1 < len(grid) and grid[y+1][x] != "0" :
                floodfill(x, y+1)
            if x + 1 <len(grid[y]) and grid[y][x+1] != "0":
                floodfill(x+1, y)
            if x - 1 >= 0 and grid[y][x-1] != "0":
                floodfill(x-1,y)
            if y - 1 >= 0 and grid[y-1][x] != "0":
                floodfill(x,y-1)

        islands = 0
        for y,row in enumerate(grid):
            for x,p in enumerate(row):
                if p == "1":
                    floodfill(x,y)
                    islands +=1
        return islands

    




        