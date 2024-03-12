class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        row = [1] * ROWS
        col = [1] * COLS

        def setRowZero(r,c):
            for c in range(COLS):
                matrix[r][c] = 0
        
        def setColZero(r,c):
            for r in range(ROWS):
                matrix[r][c] = 0
    
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    row[r] = 0
                    col[c] = 0

        for r in range(len(row)):
            if row[r] == 0:
                setRowZero(r,c)

        for c in range(len(col)):
            if col[c] == 0:
                setColZero(r,c)

        
