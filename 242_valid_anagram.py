from typing import List
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return {char: s.count(char) for char in set(s)} == {char: t.count(char) for char in set(t)}
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.isAnagram("aacc", "acca"))