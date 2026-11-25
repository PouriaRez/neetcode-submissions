class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid), len(grid[0])
        DIR = [[1,0],[-1,0],[0,1],[0,-1]]
        island_area = 0

        def bfs(r,c):

            q = deque()
            q.append((r,c))
            curr_count = 1
            grid[r][c] = 0

            while q:
                row, col = q.popleft()
                for dr, dc in DIR:
                    nr, nc = row + dr, col + dc
                    if(nr in range(ROWS) and
                        nc in range(COLS) and
                        grid[nr][nc] == 1):
                        q.append((nr,nc))
                        curr_count += 1
                        grid[nr][nc] = 0

            return curr_count

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    island_area = max(island_area,bfs(r,c))
        
        return island_area