class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        currArr = defaultdict(int)
        longest = 0
        l,r = 0,0

        while r < len(s):
            currArr[s[r]] += 1

            while currArr[s[r]] > 1:
                currArr[s[l]] -= 1
                l += 1

            longest = max(longest, r-l+1)

            r += 1

        return longest
