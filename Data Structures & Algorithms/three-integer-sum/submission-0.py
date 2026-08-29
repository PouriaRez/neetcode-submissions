class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # for every number, see if there is a two sum for that number
        '''
        [-1,0,1,2,-1,-4]
          i j

         hs = {}
         res = []
         target = nums[i](-1)

         then do the second for loop from i forward, and do 2sum on it
            complement = nums[j] - target (1)
            if hs[complement]:
               add the 3 to our result and continue
             
            
         
        -i - j = comp
        '''
        res = set()
        for i in range(len(nums)):
            target = nums[i]
            seen = set()
            for j in range(i+1, len(nums)):
                compl = -target - nums[j]
                if compl in seen:
                    res.add(tuple(sorted((target, nums[j], compl))))
                seen.add(nums[j])
        return [list(t) for t in res]