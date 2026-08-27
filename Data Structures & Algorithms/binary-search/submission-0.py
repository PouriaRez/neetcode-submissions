class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binSearch(arr, low, high, target):
            if high >= low:
                mid = low + (high - low) // 2

                if arr[mid] == target:
                    return mid
                
                elif arr[mid] > target:
                    return binSearch(arr, low, mid-1, target)

                else:
                    return binSearch(arr, mid + 1, high, target)
            else:
                return -1

        
        return binSearch(nums, 0, len(nums)-1, target)