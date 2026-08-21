class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        max_sum = float('-inf')
        total_sum = 0

        for i in range(len(nums)):

            total_sum += nums[i]

            max_sum = max(max_sum , total_sum)

            if total_sum < 0:
                total_sum = 0

            
        return max_sum 

