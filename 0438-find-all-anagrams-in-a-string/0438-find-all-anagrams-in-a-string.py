class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        pCount = [0] * 26
        wind = [0] * 26

        res = []


        if len(p) > len(s): 
            return res

       # process the pCount..

        for char in p:
            pCount[ ord(char) - ord('a')] += 1

        # process the first window..
        k = len(p)

        for i in range(k):

            wind[ ord(s[i]) - ord('a')] += 1

        if pCount == wind:

            res.append(0)

        ## process the next windows..

        for j in range(k, len(s)):

            wind[ ord(s[j]) - ord('a') ] += 1

            wind[ord(s[j-k]) - ord('a')] -= 1

            if pCount == wind:

                res.append( j-k+1 )

        return res
        



