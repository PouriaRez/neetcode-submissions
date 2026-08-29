class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
                  r
        [10,1,5,6,7,1]
            l

            prof = 6
        '''
        l = 0
        prof = float('-inf')
        for r in range(len(prices)):
            while prices[r] < prices[l]:
                l+=1 

            if prices[r] > prices[l]:
                prof = max(prof, prices[r] - prices[l])

        return prof if prof != float('-inf') else 0
            