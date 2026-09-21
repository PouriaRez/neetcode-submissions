class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bs(left, right):
            if left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    return bs(mid + 1, right)
                else:
                    return bs(left, mid-1)
            else:
                return -1

        return bs(0, len(nums)-1)