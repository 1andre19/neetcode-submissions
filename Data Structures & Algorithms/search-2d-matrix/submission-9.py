class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find possible row it might be in
        top = 0
        bottom = len(matrix) - 1
        possible_row = -1

        while top <= bottom:
            m = top + (bottom - top) // 2
            if matrix[m][0] > target:
                bottom = m - 1
            elif matrix[m][-1] < target:
                top = m + 1
            else:
                possible_row = m
                break
        
        if possible_row == -1:
            return False
        
        # binary search in possible row
        found = False
        l = 0
        r = len(matrix[0]) - 1
        while l <= r:
            m = l + (r - l) // 2
            if matrix[possible_row][m] < target:
                l = m +1
            elif matrix[possible_row][m] > target:
                r = m - 1
            else:
                return True

        return False