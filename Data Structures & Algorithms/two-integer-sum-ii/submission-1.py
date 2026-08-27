class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # [1,3,4,5,7,11] t = 9
        #       ^^


        #if sum == t:
        # return [left + 1, right + 1]
        #elif sum > t:
        # move right ptr down 1
        # if sum < t:
        #   move left ptr up
        
        left, right = 0, len(numbers)-1
        while left < right:
            currSum = numbers[left] + numbers[right]
            if currSum == target:
                return [left+1,right+1]
            elif currSum > target:
                right -= 1
            else:
                left += 1

        return []
