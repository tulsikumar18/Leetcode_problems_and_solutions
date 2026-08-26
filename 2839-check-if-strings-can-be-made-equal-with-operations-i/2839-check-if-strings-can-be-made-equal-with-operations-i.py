class Solution(object):
    def canBeEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        for i in range(2):
            j = i + 2
            if sorted([s1[i], s1[j]]) != sorted([s2[i], s2[j]]):
                return False
        return True
        