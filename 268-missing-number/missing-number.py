class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        s = 0

        while s < len(nums):
            if nums[s] != s:
                return s
            s += 1

        return s

              


        