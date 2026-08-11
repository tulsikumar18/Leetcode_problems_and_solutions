class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        res = []
        row = len(matrix)
        col = len(matrix[0])

        left = 0
        right = col - 1
        top = 0
        bottom = row - 1

        while left <= right and top <= bottom:

            # first loop..
            for j in range(left , right + 1 ):

                res.append(matrix[top][j])
            top += 1
            # second loop..
            for j in range(top , bottom + 1):

                res.append(matrix[j][right])
            right -= 1

            # 3rd loop..

            if top <= bottom:

                for j in range(right , left - 1 , -1):

                    res.append(matrix[bottom][j])

                bottom -= 1

            # 4th loop..
            if left <= right:

                for j in range(bottom, top-1 , -1):
                    res.append(matrix[j][left])

                left += 1

        return res









       