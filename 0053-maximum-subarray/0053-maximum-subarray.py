class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        total_sum  = 0 
        maxi =  float('-inf')

        for i in range(len(nums)):

            total_sum += nums[i]
            maxi = max(maxi , total_sum)

            if total_sum < 0:
                total_sum = 0

        return maxi