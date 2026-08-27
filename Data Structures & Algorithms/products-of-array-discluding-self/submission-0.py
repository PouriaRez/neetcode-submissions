class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        ans = []
        for ignore in range(len(nums)):
                total = 1
                for i, num in enumerate(nums):
                    if i == ignore:
                        continue
                    
                    total *= num
                
                ans.append(total)

        return ans
