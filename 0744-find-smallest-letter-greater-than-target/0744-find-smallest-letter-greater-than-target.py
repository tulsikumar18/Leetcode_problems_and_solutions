class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """

        res = letters[0]


        low  = 0
        high = len(letters) - 1

        while low<=high:

            mid = low + (high - low) // 2

            if letters[mid] > target:
                res = letters[mid]
                high = mid - 1

            else: 
                low = mid+1

        return res
        