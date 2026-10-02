class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        i = 0
        n = len(nums)

        nums.sort()

        while i < n-1:

            nums[i], nums[i+1] = nums[i+1], nums[i]
            i+=2

        return nums

