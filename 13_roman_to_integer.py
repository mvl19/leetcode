class Solution:
    def romanToInt(self, s: str) -> int:
        mapper = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        res = 0
        for char in range(len(s)):
            if s[char] == 'I' and char != len(s)-1 and s[char+1] in ['V', 'X']:
                res += -1
            elif s[char] == 'X' and char != len(s)-1 and s[char+1] in ['L', 'C']:
                res += -10
            elif s[char] == 'C' and char != len(s)-1 and s[char+1] in ['D', 'M']:
                res += -100
            else:
                res += mapper[s[char]]
        return res