class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        def largestRectangleArea(heights):
            max_area = 0
            stack = [] # pair : (index, height)

            for i, h in enumerate(heights):
                start = i
                while stack and stack[-1][1] > h:
                    index, height = stack.pop()
                    max_area = max(max_area, height * (i - index))
                    start = index
                stack.append((start, h))

            for i, h in stack:
                max_area = max(max_area, h * (len(heights)-i))
            
            return max_area

        if not matrix or not matrix[0]:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * cols # Histogram heights
        max_area = 0

        for row in matrix:
            for c in range(cols):
                if row[c] == '1':
                    heights[c] += 1
                else:
                   heights[c] = 0 

            # Use largest rectangle in histogram algorithm
            max_area = max(max_area, largestRectangleArea(heights))

        return max_area



