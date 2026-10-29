class Solution(object):
    def longestCommonPrefix(self, strs):
        total = ""
        index = 0

        if "" in strs:
            return ""

        if len(strs) == 1:
            return strs[0]

        while True:
            if index >= len(strs[0]):
                return total

            current = strs[0][index]

            for x in range(1, len(strs)):
                if index >= len(strs[x]) or strs[x][index] != current:
                    return total

            total = total + current
            index += 1