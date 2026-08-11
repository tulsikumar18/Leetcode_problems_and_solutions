class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        curr_sum = 0
        left = 0

        min_len = float('inf')
        if sum(nums) < target:
            return 0

        for right in range(len(nums)):

            curr_sum += nums[right]

            while curr_sum >= target:
                min_len = min(min_len, right - left + 1)
                curr_sum -= nums[left]
                left += 1

        return min_len