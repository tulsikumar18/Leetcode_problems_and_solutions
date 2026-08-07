class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        dict = {}

        for word in strs:
            count = [0] * 26

            for char in word:
                count[ord(char) - ord('a')] += 1
            
            key = str(count)
            
            if key in dict:
                dict[key].append(word)
            else:
                dict[key] = [word]

        return dict.values()
