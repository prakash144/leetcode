class Solution:
    def binary_search(self, arr, k):
        n = len(arr)
        low, high = 0, n - 1
        
        while low <= high:
            mid = (low+high) // 2
            if arr[mid] == k:
                return True
            elif arr[mid] < k:
                low = mid + 1
            else:
                high = mid - 1
        return False
        
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        
        for i in range(m):
            if matrix[i][0] <= target <= matrix[i][n-1]:
                return self.binary_search(matrix[i], target)
        return False

        