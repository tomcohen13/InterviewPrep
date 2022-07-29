def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        
        # mark visited cells
        visited = {}
        
        max_area = 0
        
        # a recursive dfs procedure
        def dfs(row, col):
            
            # case grid[i,j] is 0, halt
            if grid[row][col] == 0 or (row, col) in visited:
                return 0
            
            visited[(row,col)] = 1
            
            # find immediate neighbors
            neighbors = [(max(row - 1, 0), col), # one up 
                         (min(row + 1, m - 1), col), # one down
                         (row, max(col - 1, 0)), # one left
                         (row, min(col + 1, n - 1))  # one right
                        ]

            # return area as the sum of the neighbors plus current one
            return 1 + sum([dfs(i,j) for i,j in neighbors])
                
        
        # go over the grid to find the max_area island
        for i in range(m):
            for j in range(n):

                if grid[i][j] not in visited and grid[i][j] == 1:
                    area = dfs(i,j)
                    max_area = max(area, max_area)
                    
        return max_area
