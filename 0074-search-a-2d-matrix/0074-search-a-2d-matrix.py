class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # O(m + n), O(1)
        m, n = len(matrix), len(matrix[0])
        l, r = 0, n - 1

        while l < m and r >= 0:
            if matrix[l][r] > target:
                r -= 1
            elif matrix[l][r] < target:
                l += 1
            else:
                return True

        return False

            