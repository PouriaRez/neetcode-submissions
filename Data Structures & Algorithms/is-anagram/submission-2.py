class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = Counter(s)
        countT = Counter(t)
        if len(s) != len(t):
            return False

        for key in countS:
            if key not in countT or countT[key] != countS[key]:
                return False

        return True