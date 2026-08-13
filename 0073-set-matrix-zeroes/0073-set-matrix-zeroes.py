class Solution(object):

    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
    # Approach 1 : Brute Force..

        def modifyZero(matrix, x,y, row, col):

            for j in range(col):
                matrix[x][j] = 0

            for i in range(row):
                matrix[i][y] = 0



        row = len(matrix)
        col = len(matrix[0])

        x_idx = set()
        y_idx = set()

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    x_idx.add(i)
                    y_idx.add(j)


        # Traverse through the stored index in list and make all the index zero in the original..one..

        for i in range(row):
            for j in range(col):
                if i in x_idx or j in y_idx : 
                    matrix[i][j] = 0


        