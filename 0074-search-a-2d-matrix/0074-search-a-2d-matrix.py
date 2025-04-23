class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # Binary Search : O(log(m * n)), O(1)
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1

        while l <= r:
            mid = l + (r - l) // 2
            mid_value = matrix[mid // n][mid % n]

            if mid_value == target:
                return True
            elif mid_value > target:
                r = mid - 1
            else:
                l = mid + 1

        return False

            