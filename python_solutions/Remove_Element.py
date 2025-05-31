class Solution(object):
    def removeElement(self, nums, val):
        # Initialize a pointer for the position to insert elements that are not equal to val
        k = 0
        
        # Iterate through the array
        for i in range(len(nums)):
            # If the current element is not equal to val
            if nums[i] != val:
                # Move it to the position pointed to by k
                nums[k] = nums[i]
                # Increment k to point to the next position
                k += 1
        
        # Return the number of elements that are not equal to val
        return k