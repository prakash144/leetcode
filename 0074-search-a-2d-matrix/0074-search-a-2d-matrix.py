class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        low, high = 0, m*n - 1
        while low <= high:
            mid = (low+high) // 2
            r, c = mid // n, mid % n
            if matrix[r][c] == target:
                return True
            elif target > matrix[r][c]:
                low = mid + 1
            else:
                high = mid - 1
            
        return False

        