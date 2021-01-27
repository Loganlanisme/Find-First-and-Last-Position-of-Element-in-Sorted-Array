class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_first():
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            if left < len(nums) and nums[left] == target:
                return left
            else:
                return -1

        def find_second():
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            if right >= 0 and nums[right] == target:
                return right
            else:
                return -1

        if not nums:
            return [-1, -1]
        return [find_first(), find_second()]