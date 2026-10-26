class Solution(object):
    def romanToInt(self, s):
        a = 0
        x = 0

        lassan = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        for x in range(len(s)):
            for y in range(x + 1, x + 2):
                if y < len(s):
                    if lassan[s[x]] < lassan[s[y]]:
                        a -= lassan[s[x]]
                    else:
                        a += lassan[s[x]]
                else:
                    a += lassan[s[x]]

        return a
 


        
        
           