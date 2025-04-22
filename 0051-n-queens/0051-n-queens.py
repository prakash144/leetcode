class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set() # Tracks used columns
        pos_diag = set() # Tracks used positive diagonals (r + c)
        neg_diag = set() # Tracks used positive diagonals (r - c)

        res = []
        board = [["."] * n for _ in range(n)] # Initialize empty board

        def backtrack(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return

            for c in range(n):
                if c in col or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue

                # Place Queen
                col.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                board[r][c] = 'Q'

                backtrack(r + 1)

                # Remove Queen - backtrack
                col.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                board[r][c] = '.'

        backtrack(0)
        return res