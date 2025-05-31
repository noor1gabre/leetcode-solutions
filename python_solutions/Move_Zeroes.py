class Solution(object):
    def moveZeroes(self, nums):
        # Pointer for the position of non-zero elements
        position = 0

        # Iterate through the list
        for i in range(len(nums)):
            if nums[i] != 0:
                # Swap the current element with the element at the position pointer
                nums[position], nums[i] = nums[i], nums[position]
                position += 1

        # No need to return as the list is modified in place


        