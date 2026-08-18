class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 1:
            return 1
        if n == 2 : 
            return 2

        ways = 0 
        a = 1
        b = 2

        for i in range(3,n+1):

            ways = a + b
            a = b
            b = ways
        
        return ways


        
        