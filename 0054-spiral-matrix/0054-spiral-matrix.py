class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        res = []

        top = 0 
        right = len(matrix[0]) - 1  # 3
        bottom = len(matrix) - 1 # 2
        left = 0

        while left <= right and top <= bottom:

            # left -> right 

            for j in range(left , right + 1):
                res.append(matrix[top][j])

            top += 1

            # top -> bottom

            for j in range (top , bottom + 1):
                res.append(matrix[j][right])
            right -= 1

            # right -> left

            if top <= bottom:
                for j in range(right , left-1 , -1):
                    res.append(matrix[bottom][j])

                bottom -= 1

            # bottom -> top..
            if left <= right:
                for j in range(bottom , top-1 , -1 ):
                    res.append(matrix[j][left])
                
                left += 1

        return res


