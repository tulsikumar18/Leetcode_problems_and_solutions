class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []

        while len(nums) != 0:

            min1 = min(nums)
            nums.remove(min1)

            min2 = min(nums)
            nums.remove(min2)

            res.append(min2)
            res.append(min1)

        return res