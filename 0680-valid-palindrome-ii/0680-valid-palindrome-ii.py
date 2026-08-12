class Solution(object):

    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        def isPalindrome(left, right):
            
            while(left < right):
                if s[left] != s[right]:
                    return False

                left += 1
                right -= 1

            return True


        left = 0
        right = len(s) - 1


        while(left < right):
            if s[left] != s[right]:

                val1 = isPalindrome(left+1, right)
                val2 = isPalindrome(left, right-1)
                return val1 or val2

            left += 1
            right -= 1
        
        return True




                


        
        

        
