class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        # l, r = 0, m * n - 1

        # while l <= r:
        #     mid = l + (r - l) // 2
        #     row, col = mid // n, mid % n

        #     if matrix[row][col] > target:
        #         r = mid - 1
        #     elif matrix[row][col] < target:
        #         l = mid + 1
        #     else:
        #         return True

        # return False

        #------------------------------------------
        i, j = 0, n - 1
        while i < m and j >= 0:
            if matrix[i][j] > target:
                j -= 1
            elif matrix[i][j] < target:
                i += 1
            else:
                return True

        return False
