class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        

        def modifyZero(matrix, x,y, row, col):

            for j in range(col):
                matrix[x][j] = 0

            for i in range(row):
                matrix[i][y] = 0



        row = len(matrix)
        col = len(matrix[0])

        res = []

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    res.append([i,j])


        # Traverse through the stored index in list and make all the index zero in the original..one..

        for indexes in res:

            x = indexes[0]
            y = indexes[1]
            modifyZero(matrix, x,y, row, col)
