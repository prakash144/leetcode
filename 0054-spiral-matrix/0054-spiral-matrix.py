class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix and not matrix[0]:
            return []
        
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        result = []
        
        while top <= bottom and left <= right:
            
            # move left -> Right, across top 
            for i in range(left, right+1):
                result.append(matrix[top][i])

            top += 1

            # move top -> bottom, across right
            for i in range(top, bottom+1):
                result.append(matrix[i][right])

            right -= 1

            if top <= bottom:
                # move right -> left, across bottom
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])

                bottom -= 1

            if left <= right:
                # move bottom -> top, across left
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])

                left += 1     
            
        return result
        