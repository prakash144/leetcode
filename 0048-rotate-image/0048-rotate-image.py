class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
        for i in range(size):
            for j in range(i, size): # Start j from i to avoid redundant swaps
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        for i in range(len(matrix)):
            matrix[i].reverse()