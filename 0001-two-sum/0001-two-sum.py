class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        

        ## Optimized Approach ..

        no_idx = {}

        for i in range(len(nums)):

            rem_val = target - nums[i]

            if rem_val in no_idx:
                return [i,no_idx[rem_val]]

            else:
                no_idx[nums[i]] = i