class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """


        val_idx = {}

        for i in range(len(nums)):

            key = target - nums[i]

            if key in val_idx: 

                return [i, val_idx[key]]

            val_idx[nums[i]] = i

        

       