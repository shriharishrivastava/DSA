class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        b = 0
        c = 1

        while n != 0:
            a = n % 10
            b += a
            c *= a
            n = n / 10

        ans = c - b
        return ans