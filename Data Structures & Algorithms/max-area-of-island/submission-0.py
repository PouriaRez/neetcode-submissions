class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [[1,0],[-1,0],[0,1],[0,-1]]
        island_sum = 0

        def bfs(r,c):
            q = deque()
            q.append((r,c))
            grid[r][c] = 0
            total = 1

            while q:
                row,col = q.popleft()
                for dr,dc in DIRECTIONS:
                    nr,nc = row + dr, col + dc
                    if(
                        nr in range(ROWS) and
                        nc in range(COLS) and
                        grid[nr][nc] == 1):

                        q.append((nr,nc))
                        grid[nr][nc] = 0
                        total += 1

            return total




        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    island_sum = max(island_sum, bfs(r,c))

        return island_sum

