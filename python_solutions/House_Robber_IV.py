class Solution(object):
    def minCapability(self, nums, k):
        def can_steal(cap):
            count = 0
            i = 0
            while i < len(nums):
                if nums[i] <= cap:
                    count += 1
                    i += 1  # Skip next house to avoid adjacent robbery
                i += 1
            return count >= k

        left, right = min(nums), max(nums)
        while left < right:
            mid = (left + right) // 2
            if can_steal(mid):
                right = mid
            else:
                left = mid + 1

        return left
