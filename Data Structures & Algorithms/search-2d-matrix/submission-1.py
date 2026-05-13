class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    

        l, r = 0, len(matrix) - 1
        searchRow = None
        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                searchRow = mid
                break
            elif target < matrix[mid][0]:
                r = mid - 1
            else:
                l = mid + 1
        
        if searchRow == None:
            return False
        
        l, r = 0, len(matrix[searchRow]) - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[searchRow][mid] == target:
                return True
            elif matrix[searchRow][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
        