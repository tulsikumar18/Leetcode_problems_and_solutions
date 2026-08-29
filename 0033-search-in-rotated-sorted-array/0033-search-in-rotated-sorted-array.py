class Solution(object):


    def binarySearch(self, nums , low, high, target):
        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                return mid

            elif target > nums[mid]:
                low = mid + 1

            else:
                high = mid - 1

        return -1


    def pivotElem(self, nums, low , high):

        while low < high:
            mid = low + (high - low)// 2

            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid

        return low


    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        low = 0
        high = len(nums) - 1


        pivot = self.pivotElem(nums, low , high)

        idx = -1

        idx = self.binarySearch(nums , low, pivot-1, target)
        if idx == -1:
            idx = self.binarySearch(nums , pivot, high, target)

        return idx







        