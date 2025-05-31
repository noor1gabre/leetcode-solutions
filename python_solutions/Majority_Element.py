class Solution(object):
    def majorityElement(self, nums):
        # Step 1: Find potential candidate
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            elif candidate == num:
                count += 1
            else:
                count -= 1
        
        # Step 2: Verify if the candidate is the majority element
        count = 0
        for num in nums:
            if num == candidate:
                count += 1
        if count > len(nums) // 2:
            return candidate
        else:
            return None
            