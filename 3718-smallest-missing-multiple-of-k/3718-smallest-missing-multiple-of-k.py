class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        count = 1

        while True:

            if count * k not in nums:

                return count * k
                break
            count += 1
        