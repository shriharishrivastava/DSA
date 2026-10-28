
class Solution(object):
    def removeElement(self, nums, val):
        a = []
        b = []

        for x in range(len(nums)):
            if nums[x] == val:
                b = b + [nums[x]]
            else:
                a = a + [nums[x]]

        for x in range(len(a)):
            nums[x] = a[x]

        return len(a)


        