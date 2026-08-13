class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        

        row = len(matrix)
        col = len(matrix[0])


        # Perform Matrix Transpose , and then swap the first column with the last column value..
        for i in range(row):
            for j in range(col):

                if i < j : 
                    matrix[i][j] , matrix[j][i] = matrix[j][i], matrix[i][j]

        
        # swap the first column with the last column value..

        for i in range(row):
            for j in range((col//2)):
                k = col-1-j
                matrix[i][j] , matrix[i][k] = matrix[i][k], matrix[i][j]