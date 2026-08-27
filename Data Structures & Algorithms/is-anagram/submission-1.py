class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount = Counter(s)
        tCount = Counter(t)
        if len(s) != len(t):
            return False
            
        for key in sCount:
            if key not in tCount:
                return False
            sVal = sCount[key]
            tVal = tCount[key]
            if sVal != tVal:
                return False

        return True