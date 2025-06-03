class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        # BFS : O(R × C), O(R × C)
        row, col = len(grid), len(grid[0])
        q = deque()

        # Step 1: Add all boundary land cells to queue
        for r in range(row):
            for c in range(col):
                if (r == 0 or c == 0 or r == row - 1 or c == col - 1) and grid[r][c] == 1:
                    q.append((r, c))
                    grid[r][c] = 0 # mark visited (convert to sea)

        # Step 2: BFS from boundary land cells and flood-fill
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr , nc = r + dr, c + dc 
                if ( 0 <= nr < row and 
                    0 <= nc < col and
                    grid[nr][nc] == 1 ):
                    q.append((nr, nc))
                    grid[nr][nc] = 0 # mark visited

        # Step 3: Count remaining land cells
        return sum(cell == 1 for row in grid for cell in row)