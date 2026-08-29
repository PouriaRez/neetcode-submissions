class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ## find which row it is in
        ROWS, COLS = len(matrix), len(matrix[0])


        t,b= 0,ROWS-1

        while t <= b:
            mid = (t+b) // 2

            if matrix[mid][0] > target:
                b = mid - 1
            elif matrix[mid][-1] < target:
                t = mid + 1
            else:
                break

        ## if there was a cross-over, it could not be in the matrix
        print(t,b)
        if t > b:
            print('bad?')
            return False

        ## find which column within that row it is in
        # the row has already been found atp
        row = (t+b) // 2
        l,r = 0, COLS-1
        while l <= r:
            mid = (r+l) // 2

            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                r = mid-1
            else:
                l = mid + 1
        
        return False