class Solution(object):
    def plusOne(self, digits):
        arr = []

        num = int("".join(map(str, digits)))

        num += 1

        for x in str(num):
            arr.append(int(x))

        return arr