class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # [1,3,4,5,7,11] t = 9
        #  ^          ^
        

        l,r= 0,len(numbers)-1

        while l < r:
            total = numbers[l] + numbers[r]

            if total == target:
                return [l+1,r+1]
            elif total > target:
                r-=1
            else:
                l+=1