class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = defaultdict(int)

        for index, num in enumerate(nums):
            complement = target - num
            if complement not in hmap:
                hmap[num] = index
            else:
                return [hmap[complement], index]

